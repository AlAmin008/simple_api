from .models import employeetable
from rest_framework import serializers


class employeeserializer(serializers.ModelSerializer):

    class Meta:
        model = employeetable
        fields = '__all__'