from rest_framework.views import APIView
from rest_framework.response import Response
from task.models import Task
from task.serializers import *


class TaskDetailAPIView(APIView):
    def get(self, request, *args, **kwargs):
        task_object = Task.objects.get(pk=kwargs.get("pk"))
        serializer = TaskSerializer(instance=task_object)
        return Response(serializer.data)


class TasksView(APIView):
    def get(self, request, *args, **kwargs):
        task_list = Task.objects.all()
        serializer = TaskSerializer(task_list, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        request_data = request.data
        serializer = TaskCreateSerializer(data=request_data)
        if serializer.is_valid():
            new_task = serializer.save()
            return Response("Успешно создано", 201)
        else:
            return Response(serializer.error_messages, 400)
        
