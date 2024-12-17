from django.urls import path
from . import views

app_name = 'to_do_list' 
urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add/', views.add_task, name='add_task'),
    path('complete/<int:task_id>/', views.mark_complete, name='mark_complete'),]
