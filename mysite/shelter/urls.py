from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', include('user.urls')),
    path('pets_list/', include('pet.urls')),
    path('categories/', include('category.urls')),
    path('category/', include('category.urls')),
]