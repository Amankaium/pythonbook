from rest_framework import serializers
from task.models import Task
from users.serializers import UserSerializer


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
    
