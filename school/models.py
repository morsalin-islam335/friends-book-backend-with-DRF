from django.db import models

# Create your models here.

from personal_details.models import PersonalDetails



class School(models.Model):
    isGraduate = models.BooleanField(verbose_name = "is graduate")
    startDate = models.DateField(verbose_name = "start date")
    expectedGraduateDate = models.DateField(verbose_name = "expected graduate date")
    PersonalDetails = models.ForeignKey(PersonalDetails, on_delete= models.CASCADE, null = True, blank = True)
    name = models.CharField(max_length = 30)


