from rest_framework import serializers

from .models import Viewer


class ViewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viewer
        field = "__all__"
        