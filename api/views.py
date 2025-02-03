from django.shortcuts import render


from django.shortcuts import get_object_or_404

# Create your views here.
############## import from rest framework ###########

from rest_framework.response import Response 
from rest_framework import status 

from rest_framework.decorators import api_view
from rest_framework.views import APIView

####################################

from django.http import JsonResponse
######################################## importing models ##############
from video.models import Tag
from comment.models import Comment
from likeAndEmoji.models import Emoji
from collage.models import Collage
from person.models import Person 
from certificate.models import Certificate
from experience.models import Experience

from personal_details.models import PersonalDetails 
from photo.models import Photo
from post.models import Post
from replay.models import Replay
from school.models import School
from story.models import Story
from university.models import University
from video.models import Video
from viewer.models import Viewer


########################################################################

############## importing serializer ##############################

from video.serializers import * # video and tag serializer
from comment.serializers import CommentSerializer
from likeAndEmoji.serializers import EmojiSerializer
from collage.serializers import CollageSerializer
from person.serializers import PersonSerializer
from certificate.serializers import CertificateSerializer
from experience.serializers import ExperienceSerializer
from personal_details.serializers import PersonalDetailSerializer
from photo.serializers import PhotoSerializer
from post.serializers import PostSerializer
from replay.serializers import ReplaySerializer
from story.serializers import StorySerializer
from university.serializers import UniversitySerializer
from video.serializers import VideoSerializer
from video.serializers import TagSerializer
from viewer.serializers import ViewerSerializer

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



@api_view(["GET", "DELETE"])
def comment(request, id):
    try:
        comment = Comment.objects.get(id = id)
    
    

    except Comment.DoesNotExist:
        return Response({"error": "Comment not found"}, status = status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    if request.method == "DELETE":
        comment.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


# update api function based view
@api_view(["PUT", "GET"])
def postEmoji(request,id):
    try:
        emoji = Emoji.objects.get(id = id)
        
    
    except Emoji.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

    if request.method == "PUT":
        # update
        serializer = EmojiSerializer(emoji, data = request.data)
        # as it is  put request, we can get previous data by using request.data

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    if request.method == "GET":
        serializer = EmojiSerializer(emoji)
        return Response(serializer.data, status  =  status.HTTP_200_OK)
    


##### now working with class based view

# class CollageView(APIView): #inherit API View
#     def get(self, request, **kwargs):
#         try:
#             person = Person.objects.get(id = kwargs.get("pid"))
           
#             collage = Collage.objects.get(id=kwargs.get("cid"), PersonalDetails=person.personalDetails)
             

#         except Person.DoesNotExist:
#             return Response({"error": "There is no person with this person id"}, status = status.HTTP_404_NOT_FOUND, )
        
#         except Collage.DoesNotExist:
#             return Response({"error": "There is no Collage with this collage id"}, status = status.HTTP_404_NOT_FOUND, )
        
#         serializer = CollageSerializer(collage)
#         return Response(serializer.data, status = status.HTTP_200_OK)


class CollageView(APIView): #inherit API View
    def get(self, request, **kwargs):
        try:
           
            person = Person.objects.get(id=kwargs.get("pid"))
            collage = Collage.objects.get(
                id=kwargs.get("cid"),
                PersonalDetails= person.personalDetails  
            )
             

        except Person.DoesNotExist:
            return Response({"error": "There is no person with this person id"}, status = status.HTTP_404_NOT_FOUND, )
        
        except Collage.DoesNotExist:
            return Response({"error": "There is no Collage with this collage id"}, status = status.HTTP_404_NOT_FOUND, )
        
        serializer = CollageSerializer(collage)
        return Response(serializer.data, status = status.HTTP_200_OK)



            
        
        
        