import uuid

from django.db import models

from apps.user_auth.models import UserAuthModel


class UserModel(models.Model):
    user = models.UUIDField(
        primary_key=True, unique=True, default=uuid.uuid4, editable=False
    )
    user_name = models.CharField(max_length=250, null=False)
    user_email = models.ForeignKey(UserAuthModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ("created_at",)

    def __str__(self) -> str:
        return self.user_name
