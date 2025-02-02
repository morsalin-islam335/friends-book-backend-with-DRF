from django.urls import path 


from . views import *

urlpatterns = [
    path("videos/tags", tags),
    path("person", person ),
]