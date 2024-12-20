from django.db import models

# Create your models here.
class NoteImage(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='notes/')  # Images stored in MEDIA_ROOT/notes
    subject = models.CharField(max_length=100, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title