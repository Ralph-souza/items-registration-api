from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items_api', '0006_fix_video_item_model_and_printed_item_model_valid_null_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemsmodel',
            name='item_id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
    ]
