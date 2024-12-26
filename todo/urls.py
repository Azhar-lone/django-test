from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Homepage
    path('add/', views.add_todo, name='add_todo'),  # Add Task Page
    # path(":id",views.del_todo,name="del_todo") #remove a task
]
