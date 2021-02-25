from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def index(request):
#     return HttpResponse('<h1> this is the index page</h1>')

def index(request):
    return render(request,'pages/index.html')


def settings(request):
    return HttpResponse('<h1> this is the settings page</h1>')


def about(request):
    return HttpResponse('<h1> this is the about page</h1>')


def about(request):
    return render(request,'pages/about.html')
