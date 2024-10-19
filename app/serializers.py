from .models import employees, requests
from rest_framework import serializers

class EmployeesSerializer(serializers.ModelSerializer):

    class Meta:
        model = employees
        fields = '__all__' #('firstname','lastname','surname')
        # extra_fields = [something]

# class RequestsSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = requests
#         fields = '__all__'