from django.db import models




from django.contrib.auth.models import User



class Person(models.Model):
   

    bioData= models.TextField(max_length=100, verbose_name = "bio")


    isVerified = models.BooleanField(default = False)

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, related_name = "person")
    


    def __str__(self):
        return f"{self.user.username} data"