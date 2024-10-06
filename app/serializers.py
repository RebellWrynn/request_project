from .models import employees , requests
from rest_framework import serializers

class EmployeesSerializer(serializers.ModelSerializer):

    class Meta:
        model = employees
        fields = '__all__'


class RequestsSerializer(serializers.ModelSerializer):

    class Meta:
        model = requests
        fields = '__all__'