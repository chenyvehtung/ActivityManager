from philosopher.models import UserProfile, Activity, Application
from philosopher.forms import AddActivityForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from django.shortcuts import redirect
from django.utils import timezone

#for login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login, authenticate

from philosopher.views.function import is_organizer, is_admin, is_student, is_power

from django.db.models import Q

from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

def Homepage(request):
	limit = 6
	isOrganizer = False
	isAdmin = False
	if request.user.is_anonymous() == False: 
		isOrganizer = is_organizer(request.user)
		isAdmin = is_admin(request.user)
	activities = Activity.objects.filter(publishdate__isnull = False).filter(atstatus=0).order_by('-publishdate')
	paginator = Paginator(activities, limit)
	page = request.GET.get('page')
	try:
		activities = paginator.page(page)
	except PageNotAnInteger:
		activities = paginator.page(1)
	except EmptyPage:
		activities = paginator.page(paginator.num_pages)
	return render_to_response('templates/philosopher/homepage.html', 
		{"activities": activities, "isOrganizer":isOrganizer, "isAdmin":isAdmin}, 
		context_instance = RequestContext(request) )

def SearchActivity(request):
	limit = 6
	isOrganizer = False
	isAdmin = False
	if request.user.is_anonymous() == False: 
		isOrganizer = is_organizer(request.user)
		isAdmin = is_admin(request.user)
	q = request.GET['q']
	activities = Activity.objects.filter(publishdate__isnull = False).filter(atstatus=0).filter(Q(atname__icontains = q) | Q(atorganizer__username__icontains = q)).order_by('-publishdate')
	paginator = Paginator(activities, limit)
	page = request.GET.get('page')
	try:
		activities = paginator.page(page)
	except PageNotAnInteger:
		activities = paginator.page(1)
	except EmptyPage:
		activities = paginator.page(paginator.num_pages)
	return render_to_response('templates/philosopher/homepage.html', 
		{"activities": activities, "isOrganizer":isOrganizer, "isAdmin":isAdmin, 'queryValue': q}, 
		context_instance = RequestContext(request) )

def ActivityDetail(request, activityid):
	isOrganizer = False
	isAdmin = False
	isStudent = False
	has_right = False
	activity = get_object_or_404(Activity, pk = activityid)
	#newTen = Activity.objects.filter(publishdate__isnull = False).filter(atstatus=0).order_by('-publishdate')[:9]
	if request.user.is_anonymous() == False: 
		isOrganizer = is_organizer(request.user)
		isAdmin = is_admin(request.user)
		isStudent = is_student(request.user)
	if ( isOrganizer and activity.atorganizer.id == request.user.id ) or isAdmin:
		has_right = True
	isApplied = False
	myApplicationId = -1
	if isStudent:
		if request.user.application_set.filter(activityid = activityid).exists():
			isApplied = True
			myApplication = request.user.application_set.get(activityid = activityid)
			myApplicationId = myApplication.id
	passApplications = activity.application_set.filter(apstatus = 0)
	waitApplications = activity.application_set.filter(apstatus = 2)
	rejectApplications = activity.application_set.filter(apstatus= 1)
	finishApplications = activity.application_set.filter(apstatus = 3)
	failApplications = activity.application_set.filter(apstatus = 4)
	return render_to_response('templates/philosopher/activitydetail.html',
		{"activity": activity, "isAdmin":isAdmin, "isStudent":isStudent, "isApplied":isApplied,
		 "has_right": has_right, 'myApplicationId':myApplicationId, "passApplications":passApplications,
		 "waitApplications":waitApplications, "rejectApplications":rejectApplications, "finishApplications":finishApplications,
		 "failApplications":failApplications },
		context_instance = RequestContext(request))

@login_required
@user_passes_test(is_power)
def AddActivity(request):
	if request.method == "POST":	
		form = AddActivityForm(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit = False)
			post.atorganizer = request.user
			post.save()
			return redirect('philosopher.views.activity.ActivityDetail', activityid = post.id )
	else:
		form = AddActivityForm()
	return render_to_response('templates/philosopher/activityedit.html', {'form' : form},
		context_instance = RequestContext(request) )

@login_required
@user_passes_test(is_admin)
def ActivityExamList(request):
	activities = Activity.objects.filter(atstatus = 2)
	newTen = Activity.objects.filter(publishdate__isnull = False).filter(atstatus=0).order_by('-publishdate')[:9]
	return render_to_response('templates/philosopher/homepage.html', {'activities': activities, "newTen":newTen},
		context_instance = RequestContext(request) )

@login_required
@user_passes_test(is_admin)
def PublishActivity(request, activityid):
	activity = get_object_or_404(Activity, pk = activityid)
	activity.atstatus = 0
	activity.publishdate = timezone.now()
	activity.save()
	return redirect('philosopher.views.activity.ActivityDetail', activityid = activity.id )

#must have right to get access 
@login_required
def DeleteActivity(request, activityid):
	activity = get_object_or_404(Activity, pk = activityid)
	activity.atstatus = 1
	activity.save()
	return redirect('philosopher.views.activity.Homepage')

#also must have right 
@login_required
def EditActivity(request, activityid):
	activity = get_object_or_404(Activity, pk = activityid)
	user = activity.atorganizer
	if request.method == "POST":
		form = AddActivityForm(request.POST, request.FILES, instance=activity)
		if form.is_valid():
			activity = form.save(commit = False)
			activity.atorganizer = user
			activity.save()
			return redirect('philosopher.views.activity.ActivityDetail', activityid = activity.id )		
	else:
		form = AddActivityForm( instance=activity)
	return render_to_response('templates/philosopher/activityedit.html', {'form' : form},
		context_instance = RequestContext(request) )




