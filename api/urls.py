from django.urls import path 


from . views import *

urlpatterns = [
    path("videos/tags", tags),
    path("comment/<int:id>/", comment),
    path("person", person ),
]