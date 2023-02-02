import uuid

from django.db import models
from django.utils import timezone

from apps.items_api.models import ItemsModel, VideoItemsModel, PrintedItemsModel


class UserModel(models.Model):
    user_id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    user_name = models.CharField(max_length=250, null=False)
    user_email = models.EmailField(max_length=100, null=False)
    user_password = models.CharField(max_length=250, null=False)
    user_items = models.ForeignKey(ItemsModel, default=None, related_name="item_ids", on_delete=models.CASCADE)
    user_video_items = models.ForeignKey(
        VideoItemsModel,
        default=None,
        related_name="video_items_id",
        on_delete=models.CASCADE
    )
    user_printed_items = models.ForeignKey(
        PrintedItemsModel,
        default=None,
        related_name="printed_items_id",
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=None, editable=True, blank=True, null=True)

    class Meta:
        verbose_name = "User"
        ordering = ("created-at",)

    def __str__(self):
        return self.user_name
