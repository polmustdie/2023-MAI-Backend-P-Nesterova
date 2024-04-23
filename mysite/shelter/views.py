from django.http import JsonResponse

from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "POST"])

def index(request):
	return JsonResponse({'Stub' : 'Hi! This is our home page!'})

def shelter_profile(request):
	return JsonResponse({'Stub' : 'Profile stub is working!'})

def pets_list(request):
	return JsonResponse({'Stub' : 'List of babies in shelter is stubbed and working correctly!'})

def categories(request):
	return JsonResponse({'Stub' : 'Pets category stub is working!'})
	
def category(request, id_category):
	response = {'Stub' : 'This is category №%s and it is stubbed' % id_category}
	return JsonResponse(response)

def web_index(request):
	return JsonResponse({'Stub' : 'web index'})