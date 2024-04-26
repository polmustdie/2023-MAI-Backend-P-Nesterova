from django.contrib import admin
from shelter.models import Category, Pet, User

# Register your models here.
admin.site.register(User)
admin.site.register(Pet)
admin.site.register(Category)
