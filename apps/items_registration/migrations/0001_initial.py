from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemsModel',
            fields=[
                ('item_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('item_type', models.CharField(choices=[('video', 'video'), ('printed', 'printed')], default=None, max_length=50)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Items',
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='LoanerModel',
            fields=[
                ('loaner_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('loaner_name', models.CharField(max_length=250)),
                ('loaner_email', models.EmailField(max_length=150)),
                ('loaner_phone', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Loaner',
            },
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('user_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=250)),
                ('password', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'User',
                'ordering': ('-updated_at',),
            },
        ),
        migrations.CreateModel(
            name='VideoItemsModel',
            fields=[
                ('video_item_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('video_item_title', models.CharField(max_length=250)),
                ('video_media_type', models.CharField(choices=[('games', 'games'), ('movies', 'movies'), ('series', 'series')], default=None, max_length=250)),
                ('video_format_type', models.CharField(choices=[('dvd', 'dvd'), ('blu-ray', 'blu-ray'), ('streaming/cloud', 'streaming/cloud')], default=None, max_length=50)),
                ('launched_at', models.DateTimeField(default=None)),
                ('actor_name', models.CharField(max_length=250)),
                ('status', models.CharField(choices=[('loaned', 'loaned'), ('not loaned', 'not_loaned')], default='not_loaned', max_length=20)),
                ('loaned_since', models.DateTimeField(default=None)),
                ('returned', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='yes', max_length=50)),
                ('returned_at', models.DateTimeField(default=None)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=None)),
                ('video_item_loaned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loaners_names', to='items_registration.loanermodel')),
                ('video_item_loaner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loaners_ids', to='items_registration.loanermodel')),
                ('video_item_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items_types', to='items_registration.itemsmodel')),
            ],
            options={
                'verbose_name': 'Video Items',
                'ordering': ('-updated_at',),
            },
        ),
        migrations.CreateModel(
            name='PrintedItemsModel',
            fields=[
                ('printed_item_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('printed_item_title', models.CharField(max_length=250)),
                ('printed_media_type', models.CharField(choices=[('physical', 'physical'), ('digital', 'digital')], default=None, max_length=250)),
                ('printed_media_format', models.CharField(choices=[('book', 'book'), ('comics', 'comics'), ('digital/kindle', 'digital/kindle')], default=False, max_length=250)),
                ('launched_at', models.DateTimeField(default=None)),
                ('author_name', models.CharField(max_length=250)),
                ('status', models.CharField(choices=[('loaned', 'loaned'), ('not loaned', 'not_loaned')], default='not_loaned', max_length=20)),
                ('loaned_since', models.DateTimeField(default=None)),
                ('returned', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='yes', max_length=50)),
                ('returned_at', models.DateTimeField(default=None)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=None)),
                ('printed_item_loaned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loaner_names', to='items_registration.loanermodel')),
                ('printed_item_loaner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loaner_ids', to='items_registration.loanermodel')),
                ('printed_item_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_types', to='items_registration.itemsmodel')),
            ],
            options={
                'verbose_name': 'Printed Items',
                'ordering': ('-updated_at',),
            },
        ),
        migrations.AddField(
            model_name='itemsmodel',
            name='owner_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_ids', to='items_registration.usermodel'),
        ),
        migrations.AddField(
            model_name='itemsmodel',
            name='owner_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='names', to='items_registration.usermodel'),
        ),
    ]
