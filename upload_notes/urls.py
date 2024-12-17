from django.urls import path
from . import views

app_name = 'upload_notes'
urlpatterns = [
    path('', views.notes_list, name='notes_list'),
    path('upload/', views.upload_note, name='upload_note'),
]