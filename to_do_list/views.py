from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

# Home view
def home(request):
    return render(request, 'to_do_list/home.html')

# List all tasks
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'to_do_list/task_list.html', {'tasks': tasks})

# Create a new task
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('to_do_list:task_list')
    else:
        form = TaskForm()
    return render(request, 'to_do_list/create_task.html', {'form': form})

# Update an existing task
def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('to_do_list:task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'to_do_list/update_task.html', {'form': form, 'task': task})

# Delete a task
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.delete()
        return redirect('to_do_list:task_list')
    return render(request, 'to_do_list/delete_task.html', {'task': task})

# Mark a task as complete
def mark_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = True
    task.save()
    return redirect('to_do_list:task_list')


