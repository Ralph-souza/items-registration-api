import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [("user_auth", "0001_initial")]

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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user_email",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user_auth.userauthmodel",
                    ),
                ),
            ],
            options={
                "verbose_name": "User",
                "verbose_name_plural": "Users",
                "ordering": ("created_at",),
            },
        )
    ]
