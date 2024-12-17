from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'to_do_list/home.html')

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'to_do_list/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        category = request.POST.get('category')
        due_date = request.POST.get('due_date')
        Task.objects.create(title=title, description=description, category=category, due_date=due_date)
        return redirect('to_do_list:task_list')
    return render(request, 'to_do_list/add_task.html')

def mark_complete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('to_do_list:task_list')

def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('to_do_list:task_list')
    else:
        form = TaskForm()
    return render(request, 'to_do_list/add_task.html', {'form': form})
