from django.db import models

# Create your models here.





class PersonalDetails(models.Model):
    profession = models.CharField(max_length=40, null = True, blank = True)
    dateOfBirth = models.DateField()

