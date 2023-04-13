import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="GamesItemModel",
            fields=[
                (
                    "game_item",
                    models.AutoField(editable=False, primary_key=True, serialize=False),
                ),
                ("game_item_title", models.CharField(max_length=250)),
                (
                    "game_format_type",
                    models.CharField(
                        choices=[("physical", "physical"), ("digital", "digital")],
                        default="digital",
                        max_length=50,
                    ),
                ),
                ("producer", models.CharField(max_length=250)),
                ("release_date", models.CharField(max_length=10, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[("loaned", "loaned"), ("not_loaned", "not_loaned")],
                        default="no",
                        max_length=20,
                    ),
                ),
                (
                    "returned_date",
                    models.DateTimeField(blank=True, default=None, null=True),
                ),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "updated_at",
                    models.DateTimeField(blank=True, default=None, null=True),
                ),
            ],
            options={"verbose_name": "Game Item", "ordering": ("-updated_at",)},
        ),
        migrations.CreateModel(
            name="PrintedItemModel",
            fields=[
                (
                    "printed_item",
                    models.AutoField(editable=False, primary_key=True, serialize=False),
                ),
                ("printed_item_title", models.CharField(max_length=250)),
                (
                    "printed_media_type",
                    models.CharField(
                        choices=[("physical", "physical"), ("digital", "digital")],
                        default="physical",
                        max_length=250,
                    ),
                ),
                (
                    "printed_format_type",
                    models.CharField(
                        choices=[
                            ("book", "book"),
                            ("comics", "comics"),
                            ("digital/kindle", "digital/kindle"),
                        ],
                        default="book",
                        max_length=50,
                    ),
                ),
                ("author", models.CharField(max_length=250)),
                ("release_date", models.CharField(max_length=10, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[("loaned", "loaned"), ("not_loaned", "not_loaned")],
                        default="no",
                        max_length=20,
                    ),
                ),
                (
                    "returned_date",
                    models.DateTimeField(blank=True, default=None, null=True),
                ),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "updated_at",
                    models.DateTimeField(blank=True, default=None, null=True),
                ),
            ],
            options={"verbose_name": "Printed Item", "ordering": ("-updated_at",)},
        ),
        migrations.CreateModel(
            name="VideoItemModel",
            fields=[
                (
                    "video_item",
                    models.AutoField(editable=False, primary_key=True, serialize=False),
                ),
                ("video_item_title", models.CharField(max_length=250)),
                (
                    "video_media_type",
                    models.CharField(
                        choices=[("movies", "movies"), ("series", "series")],
                        default="movies",
                        max_length=250,
                    ),
                ),
                (
                    "video_format_type",
                    models.CharField(
                        choices=[
                            ("dvd", "dvd"),
                            ("blu-ray", "blu-ray"),
                            ("streaming/cloud", "streaming/cloud"),
                        ],
                        default="dvd",
                        max_length=50,
                    ),
                ),
                ("main_actor", models.CharField(max_length=250)),
                ("release_date", models.CharField(max_length=10, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[("loaned", "loaned"), ("not_loaned", "not_loaned")],
                        default="no",
                        max_length=20,
                    ),
                ),
                (
                    "returned_date",
                    models.DateTimeField(blank=True, default=None, null=True),
                ),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "updated_at",
                    models.DateTimeField(blank=True, default=None, null=True),
                ),
            ],
            options={"verbose_name": "Video Item", "ordering": ("-updated_at",)},
        ),
        migrations.CreateModel(
            name="ItemModel",
            fields=[
                (
                    "item",
                    models.AutoField(editable=False, primary_key=True, serialize=False),
                ),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "updated_at",
                    models.DateTimeField(blank=True, default=None, null=True),
                ),
                (
                    "game_item",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="game_items",
                        to="items_api.gamesitemmodel",
                    ),
                ),
                (
                    "printed_item",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="printed_items",
                        to="items_api.printeditemmodel",
                    ),
                ),
                (
                    "video_item",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="video_items",
                        to="items_api.videoitemmodel",
                    ),
                ),
            ],
            options={"verbose_name": "Item", "ordering": ("-updated_at",)},
        ),
    ]
