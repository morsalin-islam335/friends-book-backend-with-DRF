from rest_framework import serializers

from .models import Story


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        field = "__all__"
        