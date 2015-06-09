from philosopher.models import UserProfile, Activity
from philosopher.forms import UserForm, UserProfileForm, EUserForm, EUserProfileForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.shortcuts import redirect

#for login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login, authenticate

from philosopher.views.function import is_admin, is_organizer

def Signup(request):
	if request.method == 'POST':
		uf = UserForm(request.POST, prefix='user')
		upf = UserProfileForm(request.POST, request.FILES, prefix="userprofile")
		if uf.is_valid() * upf.is_valid():
			username = uf.clean_username()
			password = uf.clean_password2()
			uf.save()
			user = authenticate(username=username,password=password)
			userprofile = upf.save(commit = False)
			if userprofile.role == 'o':
				user.is_active = False
				userprofile.status = "w"
				user.save()
			userprofile.user = user
			userprofile.save()
			if user.is_active and userprofile.status == 'n':
				login(request, user)
			return redirect('/')
	else:
		uf = UserForm(prefix='user')
		upf = UserProfileForm(prefix='userprofile')
	return render_to_response('templates/philosopher/usersignup.html', 
		{'userform' : uf, 'userprofileform': upf},
		context_instance = RequestContext(request) )

@login_required
def  UserInfo(request, userid):
	nowuser = get_object_or_404(User, pk = userid)
	nowuserprofile = nowuser.get_profile()
	isAdmin = is_admin(request.user)
	has_right = False
	if (request.user == nowuser ) or isAdmin:
		has_right = True
	#for student 
	if nowuserprofile.role == "s":
		#0:pass; 1:reject; 2: wait; 3: finish; 4: failed
		applyApplication = nowuser.application_set.filter(apstatus = 2)
		rejectApplication = nowuser.application_set.filter(apstatus = 1)
		doingApplication = nowuser.application_set.filter(apstatus = 0)
		finishApplication = nowuser.application_set.filter(apstatus = 3)
		unfinishApplication = nowuser.application_set.filter(apstatus = 4)
		return render_to_response('templates/philosopher/studentinfo.html', 
			{"nowuser": nowuser, "nowuserprofile": nowuserprofile, "isAdmin":isAdmin, "applyApplication": applyApplication,
			"rejectApplication": rejectApplication, "doingApplication":doingApplication, "finishApplication":finishApplication,
			"unfinishApplication": unfinishApplication, "has_right": has_right, },
			context_instance = RequestContext(request))

	#for organizer
	elif nowuserprofile.role == "o":
		activities = nowuser.activity_set.all()
		return render_to_response('templates/philosopher/organizerinfo.html', 
			{"isAdmin": isAdmin, "activities":activities, "nowuser":nowuser, "has_right":has_right,
			"nowuserprofile":nowuserprofile},
			context_instance = RequestContext(request))

	#for administrator
	elif nowuserprofile.role == "a":
		nstudents = UserProfile.objects.filter(role = 's').filter(status = 'n')
		norganizers = UserProfile.objects.filter(role = 'o').filter(status = 'n')
		bstudents = UserProfile.objects.filter(role = 's').filter(status = 'b')
		borganizers = UserProfile.objects.filter(role = 'o').filter(status = 'b')
		worganizers = UserProfile.objects.filter(role = 'o').filter(status = 'w')
		nadmins = UserProfile.objects.filter(role = 'a')
		activities = Activity.objects.all()
		return render_to_response('templates/philosopher/admininfo.html', 
			{"nstudents": nstudents, "norganizers": norganizers, "bstudents": bstudents, "borganizers":borganizers,
			"worganizers":worganizers, "nadmins": nadmins, "activities": activities, "has_right":has_right,
			"nowuser":nowuser, "nowuserprofile":nowuserprofile },
			context_instance = RequestContext(request))

	else:
		return redirect('/philosopher')

@login_required
def EditInfo(request, userid):
	user = get_object_or_404(User, pk = userid)
	if (request.user == user) or is_admin(request.user):		
		userprofile = user.get_profile()
		if request.method == 'POST':
			uf = EUserForm(request.POST, prefix='user', instance = user)
			upf = EUserProfileForm(request.POST, request.FILES, prefix="userprofile", instance = userprofile)
			if uf.is_valid() * upf.is_valid():
				user = uf.save()
				userprofile = upf.save(commit = False)
				userprofile.user = user
				userprofile.save()
				return redirect('philosopher.views.user.UserInfo', userid = userid)
		else:
			uf = EUserForm(prefix='user', instance = user)
			upf = EUserProfileForm(prefix='userprofile', instance = userprofile)
	else:
		redirect('/philosopher')
	return render_to_response('templates/philosopher/edituserinfo.html', 
		{'userform' : uf, 'userprofileform': upf},
		context_instance = RequestContext(request) )	

@login_required
@user_passes_test(is_admin)
def ToggleBlack(request, userid):
	if is_admin(request.user):
		getUser = get_object_or_404(User, pk = userid)
		getProfile = getUser.get_profile()
		if getUser.is_active:
			getUser.is_active = False
			getProfile.status = 'b'
		else: 
			getUser.is_active = True
			getProfile.status = 'n'
		getUser.save()
		getProfile.save()
	return redirect('philosopher.views.user.UserInfo', userid = userid)