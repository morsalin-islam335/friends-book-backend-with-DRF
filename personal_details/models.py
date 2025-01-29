from django.db import models

# Create your models here.





class PersonalDetails(models.MOddel):
    profession = models.TextField(max_length=40, null = True, blank = True)
    dateOfBirth = models.DateField()

    