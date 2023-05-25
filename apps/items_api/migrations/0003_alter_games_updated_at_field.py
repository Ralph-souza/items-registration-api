from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items_api', '0002_games_platform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamesitemmodel',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='printeditemmodel',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='useritemsmodel',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='videositemmodel',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
