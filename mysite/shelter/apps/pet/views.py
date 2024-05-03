import json

from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from shelter.models import Pet, User, Category


def pets_list(request):
	return JsonResponse({'Stub' : 'List of babies in shelter is stubbed and working correctly!'})

def all_pets(request):
    if request.method == 'GET':
        pets = Pet.objects.all()
        return JsonResponse({
            'Pet': list(pets.values())
        })

def pet(request, id_pet):
    queryset_profile = Pet.objects.filter(id=id_pet).order_by("id")
    first_item_queryset = queryset_profile[:1]
    pet = first_item_queryset.get()
    users = pet.user_set.all()

    string = ""
    for i in range(len(users)):
        user = users[i]
        string += user.last_name + " " + user.first_name
        if i < len(users) - 1:
            string += ', '

    return JsonResponse({
        'Name': str(pet.name),
        'Description': str(pet.description),
        'Foster Parent': string
    })

def pet_by_name(request, pet_name):
    pets = (Pet.objects
                       .filter(Q(name__icontains=pet_name))
                       .all().values())
    pets_json = list(pets)
    return JsonResponse({"Pets": pets_json})


@csrf_exempt
def add_pet(request):
    if request.method == 'GET':
        return JsonResponse({"status": False, "msg": "GET request is unsupported"})

    if request.method == 'POST':
        name=json.loads(request.body)["name"]
        description = json.loads(request.body)["description"]
        parent = json.loads(request.body)["parent"]
        category_id = json.loads(request.body)["category_id"]
        print(category_id)
        print(name)

        duplicates = Pet.objects.filter(name=name)
        if len(duplicates) > 0:
            return JsonResponse({"status": False, "msg": "Duplicate"})
        new_pet = Pet()
        new_pet.name = name
        new_pet.description = description

        new_pet.category = Category.objects.get(id=category_id)
        new_pet.save()
        pet = Pet.objects.get(name=name)
        user = User.objects.get(pk=parent)
        user.pets.add(pet.id)

        return JsonResponse({"status": True, "msg": "Pet is successfully added"})
