from django.urls import path 
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *


from app.models import employees, requests
from app.serializers import EmployeesSerializer #, RequestsSerializer

def authorization(request):
    return render(request, 'authorization.html') 

def request(request):
    return render(request, 'request.html')

# Create your views here.
#-----------------------------api--------------------------------------

@api_view(['GET', 'POST'])
def employees_list(request):
    if request.method == 'GET':
        data = employees.objects.all()
        serializer = EmployeesSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        print('post')
        serializer = EmployeesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT', 'DELETE'])
def employees_detail(request, pk):
    try:
        employees = app.objects.get(pk=pk)
    except app.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = EmployeesSerializer(app, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        app.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class  EmployeesApiView(viewsets.ModelViewSet):
#     queryset = employees.objects.all()
#     serializer_class = EmployeesSerializer
#     http_method_names = ['get']
    
# class  RequestsApiView(viewsets.ModelViewSet):
#     queryset = requests.objects.all()
#     serializer_class = RequestsSerializer
#     http_method_names = ['get']
    