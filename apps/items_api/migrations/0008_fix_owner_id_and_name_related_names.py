from django.db import migrations, models

import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_api', '0003_add_editable_blank_null_to_user_items'),
        ('items_api', '0007_add_item_id_refactor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemsmodel',
            name='owner_id',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_ids', to='user_api.usermodel'),
        ),
        migrations.AlterField(
            model_name='itemsmodel',
            name='owner_name',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_names', to='user_api.usermodel'),
        ),
    ]
