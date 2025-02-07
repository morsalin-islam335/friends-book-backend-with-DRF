from django.urls import path 


from . views import *

urlpatterns = [
  
    path("persons/"), # get  all persons list
    path("persons/<int:pid>"), # get and delete single person

    path("persons/<int:pID>/shcools/>"), # get all schools
    path("persons/<int:pID>/shcools/<int:scId>"), # get, update, delete single school object
    path("persons/<int:pID>/collages/", CollageView.as_view()), # get all collages
    path("persons/<int:pID>/collages/<cID:", CollageView.as_view()), # get, update and delete single collage

    path("persons/<int:pID>/experiencses/", ExperienceListView.as_view()), # get all experiences

    path("persons/<int:pID>/experiences/<int:exID>"), # update and delete single experience

    path("persons/<int:pID>/experiences/<int:exID>/certificates"), # get all certificate
    path("persons/<int:pID>/experiences/<int:exID>/certificates/<int:cID>"), # update and delete certificate


    path("authors/<int:pID>/posts"), # get author all posts
    path("authors/<int:pID>/posts/<int:postID>"), # update and delete single post
    path("authors/<int:pID>/posts/<int:postID>/comments"), # get a post all comments
    path("authors/<int:pID>/posts/<int:postID>/comments/<int:commentID>"), # update and delete a post single comment,
    path("authors/<int:pID>/posts/<int:postID>/comments/<int:commentID/replaies>"), # get all replaies
    path("authors/<int:pID>/posts/<int:postID>/comments/<int:commentID/replaies/<int:replayID>"), #update and delete single replay

    path("authors/<int:pID>/photos"), # get author all photos
    path("authors/<int:pID>/photos/<int:photoID>"), # update and delete single photos
    path("authors/<int:pID>/photos/<int:photoID>/comments"), # get a photo all comments
    path("authors/<int:pID>/photos/<int:photoID>/comments/<int:commentID>"), # update and delete a photo single comment,
    path("authors/<int:pID>/photos/<int:photoID>/comments/<int:commentID/replaies>"), # get all replaies
    path("authors/<int:pID>/photos/<int:photoID>/comments/<int:commentID/replaies/<int:replayID>"), #update and delete single rvideos

    path("authors/<int:pID>/videos"), # get author all videos
    path("authors/<int:pID>/videos/<int:videoID>"), # update and delete single video
    path("authors/<int:pID>/videos/<int:videoID>/comments"), # get a video all comments
    path("authors/<int:pID>/videos/<int:videoID>/comments/<int:commentID>"), # update and delete a video single comment,
    path("authors/<int:pID>/videos/<int:videoID>/comments/<int:commentID/replaies>"), # get all replaies
    path("authors/<int:pID>/videos/<int:videoID>/comments/<int:commentID/replaies/<int:replayID>"), #update and delete single replay









]