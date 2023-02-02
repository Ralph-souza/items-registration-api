import uuid

from django.db import models
from django.utils import timezone

class LoanerModel(models.Model):
    loaner_id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    loaner_name = models.CharField(max_length=250, blank=False, null=False)
    loaner_email = models.EmailField(max_length=150, blank=False, null=False)
    loaner_phone = models.CharField(max_length=20, blank=False, null=False)
    video_items_loaned = models.ForeignKey(
        VideoItemsModel,
        related_name="video_items_titles",
        on_delete=models.CASCADE,
        default=None
    )
    printed_items_loaned = models.ForeignKey(
        PrintedItemsModel,
        related_name="printed_items_titles",
        on_delete=models.CASCADE,
        default=None
    )
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Loaner"

    def __str__(self):
        return self.loaner_name
