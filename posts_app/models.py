from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    text = models.TextField(verbose_name="Text")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date of creation")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date of change")
    author = models.ForeignKey(
        "users_app.User",
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name="Author",
    )
    likes = models.ManyToManyField(
        "users_app.User",
        related_name="liked_posts",
        verbose_name="Who liked",
        blank=True,
    )

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.id}. {self.title}"
