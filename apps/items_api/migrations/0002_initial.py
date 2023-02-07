from django.db import migrations, models

import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('loaner_api', '0001_initial'),
        ('user_api', '0001_initial'),
        ('items_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='videoitemmodel',
            name='loaner_name',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='video_loaner_names', to='loaner_api.loanermodel'),
        ),
        migrations.AddField(
            model_name='printeditemmodel',
            name='loaner_name',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='printed_loaner_names', to='loaner_api.loanermodel'),
        ),
        migrations.AddField(
            model_name='itemmodel',
            name='owner',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='user_api.usermodel'),
        ),
        migrations.AddField(
            model_name='itemmodel',
            name='owner_name',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_names', to='user_api.usermodel'),
        ),
        migrations.AddField(
            model_name='itemmodel',
            name='printed_item',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='printed_item_titles', to='items_api.printeditemmodel'),
        ),
        migrations.AddField(
            model_name='itemmodel',
            name='video_item',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='video_item_titles', to='items_api.videoitemmodel'),
        ),
    ]
