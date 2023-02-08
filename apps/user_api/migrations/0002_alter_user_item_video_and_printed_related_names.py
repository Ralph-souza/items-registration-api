from django.db import migrations, models

import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items_api', '0003_alter_owner_name'),
        ('user_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='user_item',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items_ids', to='items_api.itemmodel'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='user_printed_item',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='printeds_items', to='items_api.printeditemmodel'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='user_video_item',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videos_items', to='items_api.videoitemmodel'),
        ),
    ]
