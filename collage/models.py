from django.db import models

# Create your models here.
<<<<<<< HEAD
from personal_details.models import PersonalDetails



class Collage(models.Model):
    isGraduate = models.BooleanField(verbose_name = "is graduate")
    startDate = models.DateField(verbose_name = "start date")
    expectedGraduateDate = models.DateField(verbose_name = "expected graduate date")
    PersonalDetails = models.ForeignKey(PersonalDetails, on_delete= models.CASCADE, null = True, blank = True)


=======
>>>>>>> 39b37c98d3bc9c24d5cf7d24db19d899ee982453
