from rest_framework import serializers
from task.models.task import *
from .models import *


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # fields = "__all__"
        fields = ['user', 'phone_number','programming_language']


class StudentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class StudentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['phone_number','programming_language']
