import uuid

from django.db import models
from django.utils import timezone


class UserModel(models.Model):
    user_id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    user_name = models.CharField(max_length=250, null=False)
    user_email = models.EmailField(max_length=100, null=False)
    user_password = models.CharField(max_length=250, null=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=None, editable=True, blank=True, null=True)

    class Meta:
        verbose_name = "User"
        ordering = ("created-at",)

    def __str__(self):
        return self.user_name
