from django.shortcuts import render, redirect
from .models import Todo  # Import the Todo model

# Function to display all tasks
def index(request):
    todos = Todo.objects.all()  # Fetch all tasks from the database
    return render(request, 'index.html', {'todos': todos})

# Function to add a new task
def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')  # Get the title from the form
        description = request.POST.get('description')  # Get the description from the form
        Todo.objects.create(title=title, description=description)  # Add task to the database
        return redirect('index')  # Redirect to the homepage
    return render(request, 'add_todo.html')

# Function to delete  a task
# def del_todo(request):
#     if request.method=='DELETE'
    

