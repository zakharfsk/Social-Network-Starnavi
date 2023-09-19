from datetime import datetime

from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.utils.timezone import make_aware
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, views, status
from rest_framework.response import Response

from .serializers import CreatePostSerializer, PostLikesAnalyticsSerializer
from ..models import Post


param_date_from = openapi.Parameter(
    'date_from',
    openapi.IN_QUERY,
    description="field you want to order by from",
    type=openapi.TYPE_STRING
)
param_date_to = openapi.Parameter(
    'date_to',
    openapi.IN_QUERY,
    description="field you want to order by to",
    type=openapi.TYPE_STRING
)


class CreatePostAPIView(generics.CreateAPIView):
    """
    This class is used to create a post.
    """
    serializer_class = CreatePostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class LikePostAPIView(views.APIView):
    """
    This class is used to like a post.
    """
    def post(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, id=pk)

        if post.author == request.user:
            return Response({'status': 'You can\'t like your own post'}, status=status.HTTP_400_BAD_REQUEST)

        if post.likes.filter(id=request.user.id).exists():
            return Response({'status': 'User already liked this post'}, status=status.HTTP_400_BAD_REQUEST)

        post.likes.add(request.user)
        return Response({'status': 'Post liked'}, status=status.HTTP_201_CREATED)


class UnlikePostAPIView(views.APIView):
    """
    This class is used to unlike a post.
    """
    def post(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, id=pk)

        if post.author == request.user:
            return Response({'status': 'You can\'t unlike your own post'}, status=status.HTTP_400_BAD_REQUEST)

        if not post.likes.filter(id=request.user.id).exists():
            return Response({'status': 'User already unliked this post'}, status=status.HTTP_400_BAD_REQUEST)

        post.likes.remove(request.user)
        return Response({'status': 'Post unliked'}, status=status.HTTP_200_OK)


class PostLikesAnalytics(views.APIView):
    """
    This class is used to get post likes analytics.
    """
    @swagger_auto_schema(manual_parameters=[param_date_from, param_date_to])
    def get(self, request):
        date_from_str = request.GET.get('date_from')
        date_to_str = request.GET.get('date_to')

        try:
            date_from = make_aware(datetime.strptime(date_from_str, '%Y-%m-%d'))
            date_to = make_aware(datetime.strptime(date_to_str, '%Y-%m-%d'))
        except ValueError:
            return Response({"error": "Invalid date format. Please use YYYY-MM-DD."},
                            status=status.HTTP_400_BAD_REQUEST)
        except TypeError:
            return Response({"error": "Invalid date format. Please use YYYY-MM-DD."},
                            status=status.HTTP_400_BAD_REQUEST)

        analytics_data = (
            Post.objects
            .filter(created_at__range=(date_from, date_to))
            .values('created_at__date')
            .annotate(likes_count=Count('likes'))
            .order_by('created_at__date')
        )

        print(analytics_data)

        serializer = PostLikesAnalyticsSerializer(analytics_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
