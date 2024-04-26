from django.http import JsonResponse

from shelter.models import User


def shelter_profile(request):
	return JsonResponse({'Stub' : 'Profile stub is working!'})

def find_user(request, id_user):
	user = User.objects.get(pk=id_user)

	pets = User.objects.get(id=id_user).pets.all()
	return JsonResponse({
		'Name': str(user.last_name) + " " + str(user.first_name) + " "+ str(user.middle_name),
		'Description': str(user.age),
		'Foster Kids': list(pets.values())
	})

# string = ""
#     for i in range(len(pets)):
#         user = pets[i]
#         string += user.last_name + " " + user.first_name
#         if i < len(pets) - 1:
#             string += ', '

