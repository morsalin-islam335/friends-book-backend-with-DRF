from django.db import models

# Create your models here.


from person.models import Person
from django.core.exceptions import ValidationError
import os

def validate_video_file(value):
    """Validate that the uploaded file is a video."""
    ext = os.path.splitext(value.name)[1].lower()  # Get file extension
    valid_extensions = ['.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv']
    if ext not in valid_extensions:
        raise ValidationError('Unsupported file format. Please upload a video file.')



class Story(models.Model):
    person = models.ForeignKey(Person, on_delete = models.CASCADE, related_name = "story")    
    text = models.CharField(max_length = 100, null = True, blank = True)
    image = models.ImageField(upload_to="stroy/uploads/images", null = True, blank = True)
    video = models.FileField(upload_to="story/uploads/videos", null = True, blank = True, validators=[validate_video_file])





