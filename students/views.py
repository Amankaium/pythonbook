from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *


class StudentDetailAPIView(APIView):
    def get(self, request, *args, **kwargs):
        student_object = Student.objects.get(pk=kwargs.get("pk"))
        serializer = StudentsSerializer(instance=student_object)
        return Response(serializer.data)
    
    def put(self, request, *args, **kwargs):
        student_object= Student.objects.get(pk=kwargs.get("pk"))

        serializer = StudentUpdateSerializer(
            instance=student_object,
            data=request.data
        )
        if serializer.is_valid():
            student_object=serializer.save()
            return Response(serializer.data, 202)
        else:
            return Response(serializer.errors, 400)
    
    def delete(self, request, *args, **kwargs):
        student_object= Student.objects.get(pk=kwargs.get("pk"))  
        student_object.delete()
        return Response("Запись о студенте удалена", 204)  
    

class StudentsView(APIView):
    def get(self, request, *args, **kwargs):
        student_list = Student.objects.all()
        serializer = StudentsSerializer(student_list, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        request_data = request.data
        serializer = StudentCreateSerializer(data=request_data)
        if serializer.is_valid():
            new_student = serializer.save()
            return Response("Успешно создано", 201)
        else:
            return Response(serializer.error_messages, 400)
