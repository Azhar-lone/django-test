from django.shortcuts import render, redirect ,get_object_or_404

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

# Function to delete a task
def del_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)  # Get the specific task
    todo.delete()  # Delete the task
    return redirect('index')  # Redirect to the homepage
# Function to delete a task
# Function to edit a task
def edit_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)  # Get the specific task
    if request.method == 'POST':
        todo.title = request.POST.get('title')  # Update the title
        todo.description = request.POST.get('description')  # Update the description
        todo.is_completed = 'is_completed' in request.POST  # Update completion status
        todo.save()  # Save the changes
        return redirect('index')  # Redirect to the homepage
    return render(request, 'edit_todo.html', {'todo': todo})
    todo = get_object_or_404(Todo, id=todo_id)  # Get the specific task
    if request.method == 'POST':
        todo.title = request.POST.get('title')  # Update the title
        todo.description = request.POST.get('description')  # Update the description
        todo.is_completed = 'is_completed' in request.POST  # Update completion status
        todo.save()  # Save the changes
        return redirect('index')  # Redirect to the homepage