# Generated by Django 4.1.5 on 2023-02-01 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items_registration', '0003_add_created_at_to_loanermodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='printeditemsmodel',
            name='printed_item_loaned_to',
        ),
        migrations.RemoveField(
            model_name='printeditemsmodel',
            name='printed_item_loaner',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='user_items',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='user_printed_items',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='user_video_items',
        ),
        migrations.RemoveField(
            model_name='videoitemsmodel',
            name='video_item_loaned_to',
        ),
        migrations.RemoveField(
            model_name='videoitemsmodel',
            name='video_item_loaner',
        ),
    ]
