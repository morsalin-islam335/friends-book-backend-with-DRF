from django.db import models

# Create your models here.

from person.models import Person
from story.models import Story

class Viewer(models.Model):
    person = models.ForeignKey(Person, related_name= "viewers", on_delete = models.CASCADE)

    story = models.ForeignKey(Story, on_delete = models.CASCADE)

