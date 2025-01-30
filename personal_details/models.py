from django.db import models

# Create your models here.

<<<<<<< HEAD
from person.models import Person
=======


>>>>>>> 39b37c98d3bc9c24d5cf7d24db19d899ee982453


class PersonalDetails(models.Model):
    profession = models.CharField(max_length=40, null = True, blank = True)
    dateOfBirth = models.DateField(verbose_name="date of birth")
<<<<<<< HEAD
    person = models.OneToOneField(Person, on_delete= models.CASCADE)
    


=======
>>>>>>> 39b37c98d3bc9c24d5cf7d24db19d899ee982453

