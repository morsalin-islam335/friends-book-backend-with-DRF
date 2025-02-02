from django.db import models

# Create your models here.


from person.models import Person
from photo.models import Photo
from video.models import Video
from post.models import Post 


class Comment(models.Model):
    
   person = models.ForeignKey(Person, related_name = "comments", on_delete = models.CASCADE, null = True, blank = True) # after fix TODO resolve this 
   photo = models.ForeignKey(Photo, on_delete = models.CASCADE, null = True, blank = True, related_name = "comments" )
   video = models.ForeignKey(Video, on_delete = models.CASCADE, null = True, blank = True, related_name = "comments" )
   post = models.ForeignKey(Post, on_delete = models.CASCADE, null = True, blank = True, related_name = "comments" )
   text = models.CharField(max_length=500, null = True, blank = True)
   
   parent = models.ForeignKey("self", on_delete = models.CASCADE, null = True, blank = True, related_name = "replaies")

   def __str__(self):
      return f"{self.person} - {self.text[:30]}"
   
