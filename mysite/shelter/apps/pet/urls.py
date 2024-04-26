from django.urls import path
from . import views

urlpatterns = [
    path('', views.pets_list, name='pets_list'),
    path('all', views.all_pets, name='all_pets'),
    path('<int:id_pet>/', views.pet, name='find_pet'),
    path('add', views.add_pet, name='add_pet'),

]