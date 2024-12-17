from django.urls import path
from . import views

app_name = 'blog'  
urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('add/', views.add_blog, name='add_blog'),
]