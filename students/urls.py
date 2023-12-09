from django.urls import path
from .views import *

app_name = 'students'

urlpatterns = [
    path('detail/<int:pk>/', StudentDetailAPIView.as_view(), name="student-detail"),
    path('list/', StudentsView.as_view(), name="list"),

    path('list-gen/', StudentGListAPIView.as_view()),
    path('list-creategen/', StudentGCreateAPIView.as_view()),
    path('detail-gen/<int:pk>/', StudentGDetailAPIView.as_view()),
    path('detail-updategen/<int:pk>/', StudentGUpdateAPIView.as_view()),
    path('detail-destroygen/<int:pk>/', StudentGDestroyAPIView.as_view()),
]

