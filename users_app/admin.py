from django.contrib import admin

from posts_app.admin import PostAdmin
from users_app.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "last_request_to_server")
    list_display_links = ("id", "username")
    search_fields = ("username", "email")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    readonly_fields = ("last_request_to_server", "date_joined", "last_login", "password")
    inlines = (PostAdmin,)
