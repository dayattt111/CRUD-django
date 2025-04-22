# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_person, name='add_person'),
    path('', views.list_persons, name='list_persons'),
    path('update/<int:pk>/', views.update_person, name='update_person'),
    path('delete/<int:pk>/', views.delete_person, name='delete_person'),
]
