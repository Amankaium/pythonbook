from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import Mentor
from users.serializers import MentorSerializer


class MentorsView(APIView):
    def get(self, request, *args, **kwargs):
        mentor_list = Mentor.objects.all()
        mentor_serializer = MentorSerializer(mentor_list, many=True)
        json_data = mentor_serializer.data
        return Response(json_data)