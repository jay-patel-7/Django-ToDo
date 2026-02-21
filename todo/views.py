from django.shortcuts import render, redirect
from .models import Task
from django.http import HttpResponse

# Create your views here.

def addTask(request):
    # print(request.POST)
    task = request.POST['task']
    Task.objects.create(task=task)

    return redirect('home')
