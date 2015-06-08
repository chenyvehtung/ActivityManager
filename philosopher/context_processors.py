def newTen(request):
	from philosopher.models import Activity
	newTen = Activity.objects.filter(publishdate__isnull = False).filter(atstatus=0).order_by('-publishdate')[:9]
	return {"newTen": newTen, }