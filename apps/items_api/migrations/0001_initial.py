from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [("user_api", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="GamesItemModel",
            fields=[
                (
                    "game_item",
                    models.AutoField(editable=False, primary_key=True, serialize=False),
                ),
                ("game_item_title", models.CharField(max_length=150)),
                (
                    "game_format_type",
                    models.CharField(
                        choices=[("physical", "Physical"), ("digital", "Digital")],
                        default="digital",
                        max_length=20,
                    ),
                ),
                ("producer", models.CharField(max_length=150)),
                ("synopsis", models.TextField()),
                ("edition", models.CharField(max_length=20)),
                ("released_at", models.DateField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField()),
            ],
            options={
                "verbose_name": "Game item",
                "verbose_name_plural": "Games itens",
                "ordering": ("-updated_at",),
            },
        ),
        migrations.CreateModel(
            name="PrintedItemModel",
            fields=[
                (
                    "printed_item",
                    models.AutoField(editable=False, primary_key=True, serialize=False),
                ),
                ("printed_item_title", models.CharField(max_length=150)),
                (
                    "printed_media_type",
                    models.CharField(
                        choices=[("physical", "Physical"), ("digital", "Digital")],
                        default="physical",
                        max_length=20,
                    ),
                ),
                (
                    "printed_format_type",
                    models.CharField(
                        choices=[
                            ("book", "Book"),
                            ("comics", "Comics"),
                            ("digital", "Digital"),
                        ],
                        default="book",
                        max_length=20,
                    ),
                ),
                ("author", models.CharField(max_length=150)),
                ("synopsis", models.TextField()),
                ("edition", models.CharField(max_length=20)),
                ("released_at", models.DateField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField()),
            ],
            options={
                "verbose_name": "Printed item",
                "verbose_name_plural": "Printed items",
                "ordering": ("-updated_at",),
            },
        ),
        migrations.CreateModel(
            name="VideosItemModel",
            fields=[
                (
                    "video_item",
                    models.AutoField(editable=False, primary_key=True, serialize=False),
                ),
                ("video_item_title", models.CharField(max_length=150)),
                (
                    "video_media_type",
                    models.CharField(
                        choices=[("movies", "Movies"), ("series", "Series")],
                        default="movies",
                        max_length=20,
                    ),
                ),
                (
                    "video_format_type",
                    models.CharField(
                        choices=[
                            ("dvd", "DVD"),
                            ("blu_ray", "Blu-ray"),
                            ("digital", "Digital"),
                        ],
                        default="dvd",
                        max_length=20,
                    ),
                ),
                ("main_actor", models.CharField(max_length=150)),
                ("synopsis", models.TextField()),
                ("released_at", models.DateField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField()),
            ],
            options={
                "verbose_name": "Video item",
                "verbose_name_plural": "Video items",
                "ordering": ("-updated_at",),
            },
        ),
        migrations.CreateModel(
            name="UserItemsModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField()),
                (
                    "game_item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="items_api.gamesitemmodel",
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user_api.usermodel",
                    ),
                ),
                (
                    "printed_item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="items_api.printeditemmodel",
                    ),
                ),
                (
                    "video_item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="items_api.videositemmodel",
                    ),
                ),
            ],
            options={
                "verbose_name": "Item",
                "verbose_name_plural": "Items",
                "ordering": ("-updated_at",),
            },
        ),
    ]
