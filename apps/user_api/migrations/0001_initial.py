from django.db import migrations, models

import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('user_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('user_name', models.CharField(max_length=250)),
                ('user_email', models.EmailField(max_length=100)),
                ('user_password', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(blank=True, default=None, null=True)),
            ],
            options={
                'verbose_name': 'User',
                'ordering': ('-updated_at',),
            },
        ),
    ]
