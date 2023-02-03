import uuid

from django.db import models
from django.utils import timezone

from apps.items_api.models import VideoItemsModel, PrintedItemsModel


class LoanerModel(models.Model):
    loaner_id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    loaner_name = models.CharField(max_length=250, null=False)
    loaner_email = models.EmailField(max_length=150, null=False)
    loaner_phone = models.CharField(max_length=20, null=False)
    loaned_videos = models.ForeignKey(
        VideoItemsModel,
        default=None,
        related_name="loaner_video_item_titles",
        on_delete=models.CASCADE
    )
    loaned_prints = models.ForeignKey(
        PrintedItemsModel,
        default=None,
        related_name="loaner_printed_item_titles",
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=None, editable=True, blank=True, null=True)

    class Meta:
        verbose_name = "Loaner"
        ordering = ("-updated_at",)

    def __str__(self):
        return self.loaner_name
