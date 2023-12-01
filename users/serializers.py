from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Mentor


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name'
        ]


class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = [
            'name'
        ]
