from django.db import migrations, models

import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items_api', '0003_add_owner_id_and_name_and_loaner_name_to_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemsmodel',
            name='video_items',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='video_item_titles', to='items_api.videoitemsmodel'),
        ),
    ]
