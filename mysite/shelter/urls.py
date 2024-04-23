from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.shelter_profile, name='profile'),
    path('pets_list', views.pets_list, name='pets_list'),
    path('categories', views.categories, name='categories'),
    path('category/<int:id_category>/', views.category, name='category'),
]