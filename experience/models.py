from django.db import models

# Create your models here.


from person.models import Person

class Experience(models.Model):
    descriptin = models.TextField(max_length=120)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    
