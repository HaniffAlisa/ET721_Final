from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_list, name='blog_list'),  # Blog List View
    path('add/', views.add_blog, name='add_blog'),  # Create Blog
    path('<int:blog_id>/', views.blog_detail, name='blog_detail'),  # Blog Detail
    path('<int:blog_id>/edit/', views.edit_blog, name='edit_blog'),  # Edit Blog
    path('<int:blog_id>/delete/', views.delete_blog, name='delete_blog'),  # Delete Blog
]
