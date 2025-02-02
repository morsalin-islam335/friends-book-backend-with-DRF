from django.shortcuts import render

# Create your views here.
############## import from rest framework ###########

from rest_framework.response import Response 
from rest_framework import status 

from rest_framework.decorators import api_view

####################################

from django.http import JsonResponse
######################################## importing models ##############
from video.models import Tag

########################################################################

############## importing serializer ##############################

from video.serializers import * # video and tag serializer
##################################################################

def person(request):
    data ={
        "name": "Morsalin Islam",
        "profession": "backend developer"
    }

    return JsonResponse(data)
############ Function Based View ###########
@api_view(["GET","POST"])
def tags(request):
    if request.method == "GET":
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)


    elif request.method == "POST":
        serializer = TagSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
            
