from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from users.serializers import UserSerializer


class UsersView(APIView):
    def get(self, request, *args, **kwargs):
        user_list = User.objects.all()
        user_serializer = UserSerializer(user_list, many=True)
        json_data = user_serializer.data
        return Response(json_data)
