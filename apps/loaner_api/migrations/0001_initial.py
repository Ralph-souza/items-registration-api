from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [("user_api", "0001_initial"), ("items_api", "0001_initial")]

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
                ("loaner_email", models.EmailField(max_length=254)),
                ("loaner_phone", models.CharField(max_length=20)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "Loaner",
                "verbose_name_plural": "Loaners",
                "ordering": ("created_at",),
            },
        ),
        migrations.CreateModel(
            name="LoanHistory",
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
                ("returned_at", models.DateTimeField()),
                (
                    "game_item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="items_api.gamesitemmodel",
                    ),
                ),
                (
                    "loaner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="loaner_api.loanermodel",
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
        ),
        migrations.CreateModel(
            name="ItemsLoanedModel",
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
                ("since", models.DateTimeField(auto_now_add=True)),
                (
                    "game_item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="items_api.gamesitemmodel",
                    ),
                ),
                (
                    "loaner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="loaner_api.loanermodel",
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
                "verbose_name": "Item loaned",
                "verbose_name_plural": "Items loaned",
            },
        ),
    ]
