from django.db import migrations, models

import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items_api', '0002_add_video_and_printed_items_models'),
        ('loaner_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='loanermodel',
            name='loaned_prints',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='loaner_printed_item_titles', to='items_api.printeditemsmodel'),
        ),
        migrations.AddField(
            model_name='loanermodel',
            name='loaned_videos',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='loaner_video_item_titles', to='items_api.videoitemsmodel'),
        ),
    ]
