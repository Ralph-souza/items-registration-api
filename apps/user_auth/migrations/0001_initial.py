from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAuthModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth_email', models.EmailField(max_length=254)),
                ('user_password', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'User auth',
            },
        ),
    ]
