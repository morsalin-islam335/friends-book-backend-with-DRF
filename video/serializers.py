from rest_framework import serializers

from .models import Video, Tag


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        field = "__all__"
        


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        field = "__all__"
        