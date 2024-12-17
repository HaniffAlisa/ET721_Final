from django.shortcuts import render, redirect
from .models import NoteImage


# Create your views here.
def home(request):  
    return render(request, 'upload_notes/home.html')

def notes_list(request):
    notes = NoteImage.objects.all()
    return render(request, 'upload_notes/notes_list.html', {'notes': notes})

def upload_note(request):
    if request.method == "POST":
        title = request.POST.get('title')
        image = request.FILES.get('image')
        subject = request.POST.get('subject')
        NoteImage.objects.create(title=title, image=image, subject=subject)
        return redirect('upload_notes:notes_list')
    return render(request, 'upload_notes/upload_note.html')