from rest_framework import serializers

from .models import PersonalDetails


class PersonalDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalDetails
        field = "__all__"
        