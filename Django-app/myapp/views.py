from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, This is my first Project deployed using Containerization.")
