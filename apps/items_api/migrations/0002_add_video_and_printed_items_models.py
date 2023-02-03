from django.db import migrations, models

import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemsmodel',
            name='printed_items',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='printed_item_titles', to='items_api.printeditemsmodel'),
        ),
        migrations.AddField(
            model_name='itemsmodel',
            name='video_items',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='video_item_titles', to='items_api.videoitemsmodel'),
        ),
    ]
