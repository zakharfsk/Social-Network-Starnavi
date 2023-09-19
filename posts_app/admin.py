from django.contrib import admin

from posts_app.models import Post


class PostAdmin(admin.StackedInline):
    model = Post
    extra = 0
    readonly_fields = ("created_at", "updated_at", "likes", "author")
