from django.db import models



from person.models import Person

class Photo(models.Model):
    image = models.ImageField(upload_to="photo/uploads/")
    author = models.ForeignKey(Person, on_delete = models.CASCADE)
    
