from django.urls import path
from users.views import *

app_name = "usersapp"

urlpatterns = [
    path('users/', UsersView.as_view(), name='users'),
    path('mentors/', MentorsView.as_view(), name='mentors'),
]
