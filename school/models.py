from django.db import models

# Create your models here.

from personal_details.models import PersonalDetails



class School(models.Model):
    isGraduate = models.BooleanField(verbose_name = "Is Graduate")
    startDate = models.DateField(verbose_name = "Start Date")
    expectedGraduateDate = models.DateField(verbose_name = "Expected Graduate Date")
    PersonalDetails = models.ForeignKey(PersonalDetails, on_delete= models.CASCADE, null = True, blank = True)
    

