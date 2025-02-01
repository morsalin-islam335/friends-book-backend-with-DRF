from rest_framework import serializers

from . models import Collage



class CollageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collage
        fields = "__all__"


