from django.shortcuts import render


# from django.shortcuts import get_object_or_404
from django.http import HttpResponse

# Create your views here.
############## import from rest framework ###########

from rest_framework.response import Response 
from rest_framework import status 

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins



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
from school.serializers import SchoolSerializer


##################################################################

# def person(request):
#     data ={
#         "name": "Morsalin Islam",
#         "profession": "backend developer"
#     }

#     return JsonResponse(data)
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


class ExperienceListView(APIView):
    def get(self, request, **kwargs):
        try:
            experience = Experience.objects.filter(
            person = Person.objects.get(id = kwargs.get("pid"))
            )
        except Person.DoesNotExist:
            return Response({"error": "There is no person with this personID"},status = status.HTTP_404_NOT_FOUND)
        

        serializer = ExperienceSerializer(experience, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self, request, **kwargs):
        serializer = ExperienceSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)


        




######## post ##########

# now have to make actual api end point
            
class PersonListView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView,):
    serializer_class = PersonSerializer
    queryset = Person.objects.all() # just necessary for new object

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)     


# class PersonView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):

#     serializer_class = PersonSerializer
#     queryset = Person.objects.all()

#     def get(self,request, *args, **kwargs):
#         return self.retrieve(request,*args, kwargs)


    

class PersonView(mixins.RetrieveModelMixin, 
                 mixins.UpdateModelMixin, 
                 mixins.DestroyModelMixin, 
                 generics.GenericAPIView):

    serializer_class = PersonSerializer
    queryset = Person.objects.all()
  

    def get(self, request, *args, **kwargs):  
        return self.retrieve(request, *args, **kwargs)  # Correct unpacking
        


# class SchoolListview(generics.ListCreateAPIView):
#     # queryset = School.objects.all() # to apply query we have to override get_queryset method
#     serializer_class = SchoolSerializer
#     def get_queryset(self):
#         try:
#             person = Person.objects.get(pk = self.kwargs.get("pID"))
#             schools = School.objects.filter(
#                 # id = self.kwargs.get("scID"),
#                 PersonalDetails= person.personalDetails  
#             )
#             return schools
       

#         except Person.DoesNotExist:
#             raise Exception( "There is no person with this person id")
        

class SchoolListview(generics.ListCreateAPIView):
    serializer_class = SchoolSerializer

    def get_queryset(self):
        person_id = self.kwargs.get("pID")
        try:
            person = Person.objects.get(pk=person_id)
            return School.objects.filter(PersonalDetails=person.personalDetails)
        except Person.DoesNotExist:
            return School.objects.none()  # Return an empty queryset instead of raising an exception

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset:
            return Response({"error": "There is no person with this person id"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

## retrive, update and delete
class SchoolView(generics.RetrieveUpdateDestroyAPIView):
    # queryset = School.objects.all()
    serializer_class = SchoolSerializer
    # lookup_field = "id"
    # def get_queryset(self):
    #     return School.objects.filter(id = self.kwargs.get("scID"))
    lookup_field = "id"  # Match the URL parameter
    # since we work with single object,so to work with it, we have to select lookup field
    
    lookup_url_kwarg="scID"
    # formula : use main models primary key and last child model forignkey 

    def get_queryset(self):
        return School.objects.filter(id=self.kwargs.get("scID"))

# ############ in generics there is no need post and get method

class UniversityListView(generics.ListCreateAPIView):
    serializer_class = UniversitySerializer
    lookup_field = "id"
    
    def get_queryset(self):
        