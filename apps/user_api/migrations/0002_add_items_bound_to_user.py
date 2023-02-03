from django.db import migrations, models

import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items_api', '0001_initial'),
        ('user_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='user_items',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='item_ids', to='items_api.itemsmodel'),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='user_printed_items',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='printed_items_id', to='items_api.printeditemsmodel'),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='user_video_items',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='video_items_id', to='items_api.videoitemsmodel'),
        ),
    ]
