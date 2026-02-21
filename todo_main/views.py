from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    tasks = {

    }
    return render(request, 'home.html', tasks)