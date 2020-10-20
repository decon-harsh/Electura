from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

from rest_framework import serializers

from . import models

User = get_user_model()


class UploadedFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UploadedFile
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    files = UploadedFilesSerializer(many=True, read_only=True)
    # files = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = ("id", "username", "email", "password", "files")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        hashed_pass = make_password(validated_data.pop("password"))
        user = User.objects.create(**validated_data, password=hashed_pass)
        return user

    def update(self, instance, validated_data):
        print("Updating obj")
        if validated_data.get("password"):
            if validated_data.get("password") != "":

                instance.password = make_password(validated_data.pop("password"))
        updated_instance = super().update(instance, validated_data)
        return updated_instance
