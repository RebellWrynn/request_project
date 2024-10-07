from django.urls import path, include
from . import views
from rest_framework import routers

from app.views import RequestsApiView, EmployeesApiView

router = routers.DefaultRouter()
router.register(r'api/Employeeslist',EmployeesApiView)
router.register(r'api/Requestlist',RequestsApiView)

urlpatterns = [
    path('', views.authorization),  
    path('request/',views.request, name='request'),
    path('', include(router.urls))
]