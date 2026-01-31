# hello/views.py
from django.shortcuts import render

def hello_world(request):
    # Data to pass to the UI
    context = {
        'title': 'CS 302 Survey',
        'message': 'Hello World from Django in Codespaces!',
        'framework': 'Django 5.0'
    }
    return render(request, 'hello/index.html', context)