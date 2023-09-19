from rest_framework import serializers

from posts_app.models import Post


class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('id', 'author', 'created_at', 'updated_at', 'likes')


class PostLikesAnalyticsSerializer(serializers.Serializer):
    created_at__date = serializers.DateField()
    likes_count = serializers.IntegerField()
