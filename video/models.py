from django.db import models

from django.core.exceptions import ValidationError
import os

# Create your models here.

from person.models import Person

from post.models import Post



def validate_video_file(value):
    """Validate that the uploaded file is a video."""
    ext = os.path.splitext(value.name)[1].lower()  # Get file extension
    valid_extensions = ['.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv']
    if ext not in valid_extensions:
        raise ValidationError('Unsupported file format. Please upload a video file.')




class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    

class Video(models.Model):
    author = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="videos")
    title = models.CharField(max_length=255, null = True, blank = True) # in ERD it named as caption

    description = models.TextField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    video = models.FileField(upload_to="video/uploads/videos/", validators=[validate_video_file])
    thumbnail = models.ImageField(upload_to="video/uploads/thumbnails/", blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    post = models.ForeignKey(Post, on_delete = models.CASCADE, null = True, blank = True) # a post may have multiple video/videos
    

    def __str__(self):
        return self.title
