from django.urls import path
from . import views

app_name = 'upload_notes'

urlpatterns = [
    path('', views.notes_list, name='notes_list'),
    path('upload/', views.upload_note, name='upload_note'),
    path('delete/<int:note_id>/', views.delete_note, name='delete_note'),  # Delete image route
]