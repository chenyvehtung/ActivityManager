def is_organizer(user):
	userprofile = user.get_profile()
	if userprofile.role == 'o':
		return True
	else:
		return False
def is_admin(user):
	userprofile = user.get_profile()
	if userprofile.role == 'a':
		return True
	else:
		return False
def is_student(user):
	userprofile = user.get_profile()
	if userprofile.role == 's':
		return True
	else:
		return False
def is_power(user):
	userprofile = user.get_profile()
	if userprofile.role == 'o' or userprofile.role == 'a':
		return True
	return False