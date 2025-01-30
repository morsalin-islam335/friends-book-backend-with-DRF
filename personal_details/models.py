from django.db import models

# Create your models here.

from person.models import Person


class PersonalDetails(models.Model):
    profession = models.CharField(max_length=40, null = True, blank = True)
    dateOfBirth = models.DateField(verbose_name="date of birth")
    person = models.OneToOneField(Person, on_delete= models.CASCADE)
    



