import uuid

from django.db import models

from apps.user_auth.models import UserAuthModel

from apps.user_api.choices import UserGenderChoices


class UserModel(models.Model):
    user = models.UUIDField(
        primary_key=True, unique=True, default=uuid.uuid4, editable=False
    )
    name = models.CharField(max_length=250, null=False)
    birthday = models.DateField(blank=False, null=False)
    gender = models.CharField(
        choices=UserGenderChoices.choices,
        max_length=6,
        blank=False,
        null=False
    )
    email = models.ForeignKey(
        "user_auth.UserAuthModel",
        related_name="auth_relation",
        on_delete=models.CASCADE
    )
    phone = models.CharField(max_length=18, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ("created_at",)

    def __str__(self) -> str:
        return self.name
