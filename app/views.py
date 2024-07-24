from django.urls import path 
from django.shortcuts import render

def authorization(request):
    return render(request, 'authorization.html') 

def request(request):
    return render(request, 'request.html')

# Create your views here.
