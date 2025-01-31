from django.db import models

# Create your models here.


from person.models import Person
from photo.models import Photo
from video.models import Video
from post.models import Post 
from comment.models import Comment

from .constants import EMOJI_CHOICES

class Emoji(models.Model):
    emojier = models.ForeignKey(Person, on_delete = models.CASCADE, related_name="emoji")

    photo = models.ForeignKey(Photo, on_delete = models.CASCADE, null = True, blank = True) # set null and blank = true because source will only one
    video = models.ForeignKey(Video, on_delete = models.CASCADE, null = True, blank = True, related_name = "emoji")
    post = models.ForeignKey(Post, on_delete = models.CASCADE, null = True, blank = True, related_name = "emoji")
    comment = models.ForeignKey(Comment, on_delete = models.CASCADE, null = True, blank = True, related_name = "emoji")

    emoji = models.CharField(max_length=5, choices= EMOJI_CHOICES)

    def __str__(self):
        return f"{self.emojier} reacted {self.emoji}"