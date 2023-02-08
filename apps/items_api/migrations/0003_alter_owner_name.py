from django.db import migrations, models

import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_api', '0001_initial'),
        ('items_api', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemmodel',
            name='owner_name',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users_names', to='user_api.usermodel'),
        ),
    ]
