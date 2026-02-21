from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Task

def home(request):
    todo_tasks = Task.objects.filter(completed=False).order_by('-updated_at')
    completed_tasks = Task.objects.filter(completed=True).order_by('-updated_at')
    context = {
        'todo_tasks': todo_tasks,
        'completed_tasks': completed_tasks,
    }
    return render(request, 'home.html', context)