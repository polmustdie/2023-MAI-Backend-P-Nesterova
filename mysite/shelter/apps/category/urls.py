from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.categories, name='categories'),
    path('<int:id_category>/', views.category, name='category'),
    path('all', views.all_categories, name='all_categories'),
    path('add', views.add_category, name='add_category'),
]