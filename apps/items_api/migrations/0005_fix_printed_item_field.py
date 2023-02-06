from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items_api', '0004_fix_items_creation_with_null_video_and_printed_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemsmodel',
            name='printed_items',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='printed_item_titles', to='items_api.printeditemsmodel'),
        ),
    ]
