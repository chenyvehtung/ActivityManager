from philosopher.models import UserProfile, Activity, Application
from philosopher.forms import ApplicationApplyForm
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext

from philosopher.views.function import is_admin, is_organizer, is_student, is_power

from django.contrib.auth.decorators import login_required

def ApplicationApply(request, activityid):
	form = ApplicationApplyForm(request.POST)
	activity = get_object_or_404(Activity, pk = activityid)
	if form.is_valid():
		post = form.save(commit = False)
		post.activity  = activity
		post.activityid = activityid
		post.student = request.user
		post.save()
		return redirect('philosopher.views.activity.ActivityDetail', activityid = activityid)
	else:
		return redirect('/philosopher')

def ApplicationDetail(request, applicationid):
	application = get_object_or_404(Application, pk = applicationid)
	activity = application.activity
	student = application.student
	isOwner = False
	if (student == request.user ) or is_admin(request.user):
		isOwner = True
	organizer = activity.atorganizer
	isAdmin = is_admin(request.user)
	has_right = False
	if (organizer.id == request.user.id ) or isAdmin:
		has_right = True

	return render_to_response('templates/philosopher/applicationdetail.html',
	{"application": application, "has_right":has_right, "activity":activity, "student":student, 
	"isOwner":isOwner  },
	context_instance = RequestContext(request))

def ApplicationDelete(request, applicationid):
	application = get_object_or_404(Application, pk = applicationid)
	activity = application.activity
	application.delete()
	return redirect('philosopher.views.activity.ActivityDetail', activityid = activity.id )

def ApplicationHandle(request, statusid, applicationid):
	#application: 0:pass; 1:reject; 2: wait; 3: finish; 4: failed
	#statusid: 1:reject; 2:pass; 3:finish; 4:failed; 
	application = get_object_or_404(Application, pk = applicationid)
	student = application.student
	studentinfo = student.get_profile()
	activity = application.activity
	if statusid == '1':
		application.apstatus = 1
	elif statusid == '2':
		application.apstatus = 0
	elif statusid == '3':
		application.apstatus = 3
		studentinfo.attimes += activity.athours
		studentinfo.save()
	elif statusid == '4':
		application.apstatus = 4
	else:
		application.apstatus = 2
	application.save()
	return redirect('philosopher.views.activity.ActivityDetail', activityid = activity.id)

@login_required
def ApplicationEdit(request, applicationid):
	application= get_object_or_404(Application, pk = applicationid)
	activity = application.activity
	nowuser = application.student
	if (nowuser == request.user ) or is_admin(request.user):
		if request.method == "POST":
			form = ApplicationApplyForm(request.POST, instance=application)
			if form.is_valid():
				application = form.save(commit = False)
				application.save()
				return redirect('philosopher.views.application.ApplicationDetail', applicationid = application.id )		
		else:
			form = ApplicationApplyForm(instance=application)
	else:
		return redirect('/philosopher')
	return render_to_response('templates/philosopher/applicationedit.html', 
		{'form' : form, 'nowuser':nowuser, 'activity':activity },
		context_instance = RequestContext(request) )
