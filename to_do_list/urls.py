from django.urls import path
from . import views

app_name = 'to_do_list'

urlpatterns = [
    path('', views.task_list, name='task_list'),  # Task List
    path('create/', views.create_task, name='create_task'),  # Create Task
    path('update/<int:task_id>/', views.update_task, name='update_task'),  # Update Task
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),  # Delete Task
    path('complete/<int:task_id>/', views.mark_complete, name='mark_task_complete'),  # Mark Complete
]
