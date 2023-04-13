import uuid

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [("items_api", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="UserModel",
            fields=[
                (
                    "user",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("user_name", models.CharField(max_length=250)),
                ("user_email", models.EmailField(max_length=100)),
                ("user_password", models.CharField(max_length=250)),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "updated_at",
                    models.DateTimeField(blank=True, default=None, null=True),
                ),
                (
                    "user_item",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="items_api.itemmodel",
                    ),
                ),
            ],
            options={"verbose_name": "User", "ordering": ("-updated_at",)},
        )
    ]
