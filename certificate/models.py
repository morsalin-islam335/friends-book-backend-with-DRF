from django.db import models

# Create your models here.

from experience.models import Experience

class Certificate(models.Model):
    experience = models.ForeignKey(Experience, on_delete= models.CASCADE, null = True, blank = True)
    certificate = models.ImageField(upload_to="certificate/media/uploads/")