from django.contrib.auth.models import User
from rest_framework import serializers
from .models import FreeLancer


class FreelancerUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "username", "email", "date_joined")


class FreelancerSerializer(serializers.ModelSerializer):
    user = FreelancerUserSerializer(read_only=True)

    class Meta:
        model = FreeLancer
        fields = ("user", "name", "family", "father_name")
