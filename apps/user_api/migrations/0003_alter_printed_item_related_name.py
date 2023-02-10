from django.db import migrations, models

import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items_api', '0004_alter_item_model_owner_name_related_name'),
        ('user_api', '0002_alter_user_item_video_and_printed_related_names'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='user_printed_item',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='printed_items', to='items_api.printeditemmodel'),
        ),
    ]
