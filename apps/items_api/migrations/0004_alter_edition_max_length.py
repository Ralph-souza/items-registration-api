from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items_api', '0003_alter_games_updated_at_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamesitemmodel',
            name='edition',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='printeditemmodel',
            name='edition',
            field=models.CharField(max_length=50),
        ),
    ]
