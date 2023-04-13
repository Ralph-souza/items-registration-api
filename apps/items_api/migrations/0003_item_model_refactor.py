from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [("items_api", "0002_initial")]

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
        migrations.RenameField(
            model_name="printeditemmodel",
            old_name="loaned_date",
            new_name="returned_date",
        ),
        migrations.RenameField(
            model_name="videoitemmodel",
            old_name="loaned_date",
            new_name="returned_date",
        ),
        migrations.RemoveField(model_name="itemmodel", name="item_type"),
        migrations.RemoveField(model_name="itemmodel", name="owner"),
        migrations.RemoveField(model_name="itemmodel", name="owner_name"),
        migrations.RemoveField(model_name="printeditemmodel", name="edition"),
        migrations.RemoveField(model_name="printeditemmodel", name="loaner_name"),
        migrations.RemoveField(model_name="printeditemmodel", name="returned_at"),
        migrations.RemoveField(model_name="printeditemmodel", name="returned_status"),
        migrations.RemoveField(model_name="videoitemmodel", name="loaner_name"),
        migrations.RemoveField(model_name="videoitemmodel", name="returned_at"),
        migrations.RemoveField(model_name="videoitemmodel", name="returned_status"),
        migrations.AlterField(
            model_name="itemmodel",
            name="printed_item",
            field=models.ForeignKey(
                blank=True,
                default=None,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="printed_items",
                to="items_api.printeditemmodel",
            ),
        ),
        migrations.AlterField(
            model_name="itemmodel",
            name="video_item",
            field=models.ForeignKey(
                blank=True,
                default=None,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="video_items",
                to="items_api.videoitemmodel",
            ),
        ),
        migrations.AlterField(
            model_name="printeditemmodel",
            name="printed_format_type",
            field=models.CharField(
                choices=[
                    ("book", "book"),
                    ("comics", "comics"),
                    ("digital/kindle", "digital/kindle"),
                ],
                default="book",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="printeditemmodel",
            name="printed_media_type",
            field=models.CharField(
                choices=[("physical", "physical"), ("digital", "digital")],
                default="physical",
                max_length=250,
            ),
        ),
        migrations.AlterField(
            model_name="videoitemmodel",
            name="video_media_type",
            field=models.CharField(
                choices=[("movies", "movies"), ("series", "series")],
                default="movies",
                max_length=250,
            ),
        ),
        migrations.AddField(
            model_name="itemmodel",
            name="game_item",
            field=models.ForeignKey(
                blank=True,
                default=None,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="game_items",
                to="items_api.gamesitemmodel",
            ),
        ),
    ]
