from django.urls import path
from .views import *

app_name = 'students'

urlpatterns = [
    path('detail/<int:pk>/', StudentDetailAPIView.as_view(), name="student-detail"),
    path('list/', StudentsView.as_view(), name="list"),
]

