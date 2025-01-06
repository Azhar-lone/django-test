from django.urls import path
from . import views

urlpatterns = [
path('add/', views.add_todo, name='add_todo'),  # Add Task Page CREATE
    path('', views.index, name='index'),  # Homepage READ 
    path('edit/<int:todo_id>/', views.edit_todo, name='edit_todo'), #edit a task UPDATE
    path('delete/<int:todo_id>/', views.del_todo, name='del_todo'), #remove a task DELETE
]
