from django.urls import path
from task.views.task import TaskDetailAPIView

app_name = 'task'

urlpatterns = [
    path('detail/<int:pk>/', TaskDetailAPIView.as_view(), name="task-detail"),
]