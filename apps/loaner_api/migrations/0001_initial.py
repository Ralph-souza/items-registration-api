import uuid

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [("items_api", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="LoanerModel",
            fields=[
                (
                    "loaner",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("loaner_name", models.CharField(max_length=250)),
                ("loaner_email", models.EmailField(max_length=150)),
                ("loaner_phone", models.CharField(max_length=20)),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "updated_at",
                    models.DateTimeField(blank=True, default=None, null=True),
                ),
                (
                    "loaned_printed_item",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="loaner_printed_item_titles",
                        to="items_api.printeditemmodel",
                    ),
                ),
                (
                    "loaned_video_item",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="loaner_video_item_titles",
                        to="items_api.videoitemmodel",
                    ),
                ),
            ],
            options={"verbose_name": "Loaner", "ordering": ("-updated_at",)},
        )
    ]
