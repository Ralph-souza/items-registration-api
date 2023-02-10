from django.db import migrations, models

import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_api', '0002_alter_user_item_video_and_printed_related_names'),
        ('items_api', '0003_alter_owner_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemmodel',
            name='owner_name',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='names', to='user_api.usermodel'),
        ),
    ]
