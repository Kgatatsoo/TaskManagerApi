from rest_framework import serializers
from.models import taskmanagerapp

class taskmanagerappserializer(serializers.ModelSerializer):
    class Meta:
        model = taskmanagerapp
        fields ='__all__'
        read_only_fields = ['user']