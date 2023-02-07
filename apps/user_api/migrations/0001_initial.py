from django.db import migrations, models

import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('items_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('user', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('user_name', models.CharField(max_length=250)),
                ('user_email', models.EmailField(max_length=100)),
                ('user_password', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('user_item', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item_ids', to='items_api.itemmodel')),
                ('user_printed_item', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='printed_items', to='items_api.printeditemmodel')),
                ('user_video_item', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='video_items', to='items_api.videoitemmodel')),
            ],
            options={
                'verbose_name': 'User',
                'ordering': ('-updated_at',),
            },
        ),
    ]
