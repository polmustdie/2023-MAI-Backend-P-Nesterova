import json

from django.http import JsonResponse
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt

from shelter.models import Category


def categories(request):
    return JsonResponse({'Stub': 'Pets category stub is working!'})


def category(request, id_category):
    obj = Category.objects.get(pk=id_category)
    response = {'Stub': 'This is category №'+ smart_str(id_category) + " "+  str(obj) +' and it is stubbed'}
    return JsonResponse(response)


def all_categories(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        return JsonResponse({
            'Category': list(categories.values())
        })


@csrf_exempt
def add_category(request):
    if request.method == 'GET':
        return JsonResponse({"status": False, "msg": "GET request is unsupported"})

    if request.method == 'POST':
        name=json.loads(request.body)["category_name"]
        print(name)

        duplicates = Category.objects.filter(title=name)
        if len(duplicates) > 0:
            return JsonResponse({"status": False, "msg": "Duplicate"})

        new_category = Category()
        new_category.title = name
        new_category.save()

        return JsonResponse({"status": True, "msg": "Category is successfully added"})