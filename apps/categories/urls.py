# apps/categories/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_list, name='category-list'),
]
