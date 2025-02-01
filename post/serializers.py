from rest_framework import serializers

from .models import Post


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        field = "__all__"
        