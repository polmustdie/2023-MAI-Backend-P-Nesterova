from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.shelter_profile, name='profile'),
    path('<int:id_user>/', views.find_user, name='find_user'),
]