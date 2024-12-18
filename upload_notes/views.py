from django.shortcuts import render, redirect, get_object_or_404
from .models import NoteImage
from .forms import NoteImageForm


# Create your views here.
def home(request):  
    return render(request, 'upload_notes/home.html')

def notes_list(request):
    notes = NoteImage.objects.all()
    return render(request, 'upload_notes/notes_list.html', {'notes': notes})

def upload_note(request):
    if request.method == "POST":
        form = NoteImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_notes:notes_list')
    else:
        form = NoteImageForm()
    return render(request, 'upload_notes/upload_note.html', {'form': form})

def delete_note(request, note_id):
    note = get_object_or_404(NoteImage, id=note_id)
    if request.method == "POST":
        note.delete()
        return redirect('upload_notes:notes_list')
    return render(request, 'upload_notes/delete_note.html', {'note': note})