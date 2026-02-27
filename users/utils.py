from funsionario.models import staff

def a_user_emp(user):
	objects = staffuser.objects.filter(empuser__user=user).prefetch_related('empuser').first()
	obj = ""
	if objects: obj = objects
	return obj
