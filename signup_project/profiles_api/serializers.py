from rest_framework import serializers

from profiles_api.models import Profile

class PostProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["name", "surname", "email", "phone"]

class GetProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["name", "surname", "email", "phone", "validated_email", "validated_phone"]