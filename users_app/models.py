from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    last_request_to_server = models.DateTimeField(
        verbose_name="Last request to server",
        auto_now_add=True,
        help_text="The date and time of the last request to the server.",
    )

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ("id",)
