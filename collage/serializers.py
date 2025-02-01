from rest_framework import serializers

from . models import Collage



class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collage
        fields = "__all__"


