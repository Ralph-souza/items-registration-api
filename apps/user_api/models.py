import uuid

from django.db import models
from django.utils import timezone

from apps.items_api.models import ItemModel


class UserModel(models.Model):
    user = models.UUIDField(
        primary_key=True, unique=True, default=uuid.uuid4, editable=False
    )
    user_name = models.CharField(max_length=250, null=False)
    user_email = models.EmailField(max_length=100, null=False)
    user_password = models.CharField(max_length=250, null=False)
    user_item = models.ForeignKey(
        ItemModel,
        default=None,
        related_name="items",
        editable=True,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(
        default=None, editable=True, blank=True, null=True
    )

    class Meta:
        verbose_name = "User"
        ordering = ("-updated_at",)

    def __str__(self):
        return self.user_name
