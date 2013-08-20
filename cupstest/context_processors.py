from django.conf import settings

def django_settings(request):
	result = {}
	for s in dir(settings):
		result[s] = getattr(settings, s)
	return result