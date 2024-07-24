from django.urls import path
from . import views

urlpatterns = [
    path('', views.authorization),  
    path('request/',views.request, name="request")
]