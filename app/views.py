from django.urls import path 
from django.shortcuts import render
from rest_framework import viewsets

from app.models import employees, requests
from app.serializers import EmployeesSerializer, RequestsSerializer

def authorization(request):
    return render(request, 'authorization.html') 

def request(request):
    return render(request, 'request.html')

# Create your views here.
#-----------------------------api--------------------------------------

class  EmployeesApiView(viewsets.ModelViewSet):
    queryset = employees.objects.all()
    serializer_class = EmployeesSerializer
    http_method_names = ['get']
    
class  RequestsApiView(viewsets.ModelViewSet):
    queryset = requests.objects.all()
    serializer_class = RequestsSerializer
    http_method_names = ['get']
    