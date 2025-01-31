from django.db import models



from person.models import Person

# from post.models import Post



class Photo(models.Model):
    image = models.ImageField(upload_to="photo/uploads/")
    author = models.ForeignKey(Person, on_delete = models.CASCADE)

    # post = models.ForeignKey(Post, on_delete= models.CASCADE, null = True, blank = True) # a post may  have multiple photo/s

    
