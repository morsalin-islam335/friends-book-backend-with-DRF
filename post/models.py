from django.db import models

# Create your models here.


from person.models import Person

class Post(models.Model):
    author = models.ForeignKey(Person, on_delete = models.CASCADE)
    description = models.CharField(max_length=2000, null = True, blank = True)
    #photo
    #video
    #emoji
    #comment
    