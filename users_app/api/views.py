from django.contrib.auth.hashers import make_password
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, views
from rest_framework.response import Response

from .serializers import RegisterUserSerializer, UserActivitySerializer


class RegisterUserAPIView(generics.CreateAPIView):
    """
    This class is used to register a user.
    """
    serializer_class = RegisterUserSerializer
    permission_classes = []

    def perform_create(self, serializer):
        password = make_password(serializer.validated_data.get("password"))
        serializer.save(password=password)


class UserActivityAPIView(views.APIView):
    """
    This class is used to get user activity.
    """
    @swagger_auto_schema(
        operation_description="Get user activity",
        responses={
            200: UserActivitySerializer(),
        },
    )
    def get(self, request):
        user = request.user
        serializer = UserActivitySerializer(user)
        return Response(serializer.data)
