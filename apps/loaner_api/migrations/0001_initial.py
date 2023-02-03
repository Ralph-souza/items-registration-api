from django.db import migrations, models

import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoanerModel',
            fields=[
                ('loaner_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('loaner_name', models.CharField(max_length=250)),
                ('loaner_email', models.EmailField(max_length=150)),
                ('loaner_phone', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(blank=True, default=None, null=True)),
            ],
            options={
                'verbose_name': 'Loaner',
                'ordering': ('-updated_at',),
            },
        ),
    ]
