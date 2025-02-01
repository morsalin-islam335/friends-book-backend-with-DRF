from django.db import models

# Create your models here.




from person.models import Person

from story.models import Story 






class Replay(models.Model):
    #person
    replayer = models.ForeignKey(Person, on_delete = models.CASCADE, related_name = "story_replaies")

    #story

    story = models.ForeignKey(Story, on_delete= models.CASCADE, related_name = "replaies")

    #instance
    parent = models.ForeignKey("self", null = True, blank = True, on_delete = models.CASCADE)

    #text

    text = models.CharField(max_length = 700)
    #image
    image = models.ImageField(upload_to = "replay/uploads/image")

    #emoji