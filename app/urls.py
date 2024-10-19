from django.urls import path, re_path, include
from . import views
from rest_framework import routers

# from app.views import RequestsApiView, EmployeesApiView

# router = routers.DefaultRouter()
# router.register(r'api/Employeeslist',EmployeesApiView)
# router.register(r'api/Requestlist',RequestsApiView)

urlpatterns = [
    path('', views.authorization),  
    path('employees/',views.employees_list),
    path('request/',views.request)
    # re_path(r'^api/employees/$', views.employees_list),
    # re_path(r'^api/employees/(\d+)$', views.employees_list)
]