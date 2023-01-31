from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items_registration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemsmodel',
            name='printed_items',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='prints_items_titles', to='items_registration.printeditemsmodel'),
        ),
        migrations.AddField(
            model_name='itemsmodel',
            name='video_items',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='videos_items_titles', to='items_registration.videoitemsmodel'),
        ),
        migrations.AddField(
            model_name='loanermodel',
            name='printed_items_loaned',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='printed_items_titles', to='items_registration.printeditemsmodel'),
        ),
        migrations.AddField(
            model_name='loanermodel',
            name='video_items_loaned',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='video_items_titles', to='items_registration.videoitemsmodel'),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='user_items',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='items_ids', to='items_registration.itemsmodel'),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='user_printed_items',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='printed_item_titles', to='items_registration.printeditemsmodel'),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='user_video_items',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='video_item_titles', to='items_registration.videoitemsmodel'),
        ),
    ]
