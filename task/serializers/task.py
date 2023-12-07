from rest_framework import serializers
from task.models import Task
from users.serializers import UserSerializer
from django.contrib.auth.models import User


class TaskSerializer(serializers.ModelSerializer):
    # views_by = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # views_by = serializers.StringRelatedField(many=True)
    views_by = UserSerializer(many=True, read_only=True)
    views_count = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ['name', 'description', 'views_by', 'views_count']
    
    def get_views_count(self, task_obj):
        return task_obj.views_by.count()


class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class TaskAddViewSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='views_by.id')
    
    class Meta:
        model = Task
        fields = ['user_id']
    
    def update(self, instance, validated_data):
        user_id = validated_data.get('user_id')
        print(user_id)
        user_object = User.objects.get(id=user_id)
        instance.views_by.add(user_object)
        return instance
