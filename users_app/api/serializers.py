from rest_framework import serializers

from users_app.models import User


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "password", "email", "first_name", "last_name")
        extra_kwargs = {"password": {"write_only": True}}


class UserActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("last_login", "last_request_to_server")
        read_only_fields = ("last_login", "last_request_to_server")
