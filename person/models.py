from django.db import models

# Create your models here.
<<<<<<< HEAD


from django.contrib.auth.models import User



class Person(models.Model):
   

    bioData= models.TextField(max_length=100, verbose_name = "bio")


    isVerified = models.BooleanField(default = False)

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)


#after crash
=======
>>>>>>> 39b37c98d3bc9c24d5cf7d24db19d899ee982453
