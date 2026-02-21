from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.http import HttpResponse


# Create your views here.

def addTask(request):
    # print(request.POST)
    task = request.POST['task']
    Task.objects.create(task=task)

    return redirect('home')

def mark_as_done(request, id):
    # task = Task.objects.get(id=id)
    task = get_object_or_404(Task, id=id)
    task.completed = True
    task.save()
    return redirect('home')

def mark_as_undone(request, id):
    task = get_object_or_404(Task, id=id)
    task.completed = False
    task.save()
    return redirect('home')

def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('home')

def edit_task(request, id):
    get_task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        new_task = request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect('home')
    else:
        context = {
            'get_task': get_task,
        }
        return render(request, 'edit_task.html', context)