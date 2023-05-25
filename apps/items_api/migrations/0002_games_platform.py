from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamesitemmodel',
            name='platform',
            field=models.CharField(choices=[('playstation 4', 'Playstation 4'), ('nintendo switch', 'Nintendo Switch')], default='playstation 4', max_length=100),
        ),
    ]
