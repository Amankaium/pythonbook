from rest_framework.views import APIView
from rest_framework.response import Response
from task.models import Task
from task.serializers import TaskAddViewSerializer
from django.contrib.auth.models import User



class AddViewAPI(APIView):
    def put(self, request, *args, **kwargs):
        task_object = Task.objects.get(pk=kwargs.get("task_pk"))
        serializer = TaskAddViewSerializer(
            instance=task_object,
            data=request.data
        )
        if serializer.is_valid():
            user_id = serializer.validated_data["views_by"]["id"]
            user_object = User.objects.get(id=user_id)
            task_object.views_by.add(user_object)
            task_object.save()
            return Response("Success", 201)
        else:
            return Response(serializer.error_messages, 400)
        