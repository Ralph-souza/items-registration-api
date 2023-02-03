from django.db import migrations, models

import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items_api', '0002_add_video_and_printed_items_models'),
        ('user_api', '0002_add_items_bound_to_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='user_items',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item_ids', to='items_api.itemsmodel'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='user_printed_items',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='printed_items_id', to='items_api.printeditemsmodel'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='user_video_items',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='video_items_id', to='items_api.videoitemsmodel'),
        ),
    ]
