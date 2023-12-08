from django.urls import path
from task.views.task import *
from task.views.add_view import *

app_name = 'task'

urlpatterns = [
    path('detail/<int:pk>/', TaskDetailAPIView.as_view(), name="task-detail"),
    path('list/', TasksView.as_view(), name='list'),

    path('detail-generic/<int:pk>/', TaskGenericDetailAPIView.as_view(), name="task-detail-generic"),
    path('list-generic/', TasksGenericView.as_view(), name='list-generic'),

    path('add-view/<int:task_pk>/', AddViewAPI.as_view(), name='add-view'),
]
