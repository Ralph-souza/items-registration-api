from django.db import migrations, models

import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loaner_api', '0003_add_editable_blank_and_null_to_loaner_items'),
        ('user_api', '0003_add_editable_blank_null_to_user_items'),
        ('items_api', '0002_add_video_and_printed_items_models'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemsmodel',
            name='owner_id',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users_ids', to='user_api.usermodel'),
        ),
        migrations.AddField(
            model_name='itemsmodel',
            name='owner_name',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users_names', to='user_api.usermodel'),
        ),
        migrations.AddField(
            model_name='printeditemsmodel',
            name='loaner_name',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='printed_loaner_names', to='loaner_api.loanermodel'),
        ),
        migrations.AddField(
            model_name='videoitemsmodel',
            name='loaner_name',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='video_loaner_names', to='loaner_api.loanermodel'),
        ),
    ]
