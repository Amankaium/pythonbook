from django.urls import path
from task.views.task import *
from task.views.add_view import *

app_name = 'task'

urlpatterns = [
    path('detail/<int:pk>/', TaskDetailAPIView.as_view(), name="task-detail"),
    path('list/', TasksView.as_view(), name='list'),
    path('add-view/<int:task_pk>/', AddViewAPI.as_view(), name='add-view'),
]
