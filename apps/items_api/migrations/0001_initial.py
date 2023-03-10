from django.db import migrations, models

import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemModel',
            fields=[
                ('item', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('item_type', models.CharField(choices=[('video', 'video'), ('printed', 'printed')], default='video', max_length=50)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(blank=True, default=None, null=True)),
            ],
            options={
                'verbose_name': 'Item',
                'ordering': ('-updated_at',),
            },
        ),
        migrations.CreateModel(
            name='PrintedItemModel',
            fields=[
                ('printed_item', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('printed_item_title', models.CharField(max_length=250)),
                ('printed_media_type', models.CharField(choices=[('physical', 'physical'), ('digital', 'digital')], default='games', max_length=250)),
                ('printed_format_type', models.CharField(choices=[('book', 'book'), ('comics', 'comics'), ('digital/kindle', 'digital/kindle')], default='dvd', max_length=50)),
                ('release_date', models.CharField(max_length=10, null=True)),
                ('edition', models.CharField(blank=True, max_length=10, null=True)),
                ('author', models.CharField(max_length=250)),
                ('status', models.CharField(choices=[('loaned', 'loaned'), ('not_loaned', 'not_loaned')], default='no', max_length=20)),
                ('loaned_date', models.DateTimeField(blank=True, default=None, null=True)),
                ('returned_status', models.CharField(blank=True, choices=[('yes', 'yes'), ('no', 'no')], default=None, max_length=50, null=True)),
                ('returned_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(blank=True, default=None, null=True)),
            ],
            options={
                'verbose_name': 'Printed Item',
                'ordering': ('-updated_at',),
            },
        ),
        migrations.CreateModel(
            name='VideoItemModel',
            fields=[
                ('video_item', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('video_item_title', models.CharField(max_length=250)),
                ('video_media_type', models.CharField(choices=[('games', 'games'), ('movies', 'movies'), ('series', 'series')], default='games', max_length=250)),
                ('video_format_type', models.CharField(choices=[('dvd', 'dvd'), ('blu-ray', 'blu-ray'), ('streaming/cloud', 'streaming/cloud')], default='dvd', max_length=50)),
                ('release_date', models.CharField(max_length=10, null=True)),
                ('main_actor', models.CharField(max_length=250)),
                ('status', models.CharField(choices=[('loaned', 'loaned'), ('not_loaned', 'not_loaned')], default='no', max_length=20)),
                ('loaned_date', models.DateTimeField(blank=True, default=None, null=True)),
                ('returned_status', models.CharField(blank=True, choices=[('yes', 'yes'), ('no', 'no')], default=None, max_length=50, null=True)),
                ('returned_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(blank=True, default=None, null=True)),
            ],
            options={
                'verbose_name': 'Video Item',
                'ordering': ('-updated_at',),
            },
        ),
    ]
