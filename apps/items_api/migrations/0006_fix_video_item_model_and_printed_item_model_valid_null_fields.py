from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items_api', '0005_fix_printed_item_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='printeditemsmodel',
            name='loaned_date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='printeditemsmodel',
            name='release_date',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='printeditemsmodel',
            name='returned_at',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='printeditemsmodel',
            name='status',
            field=models.CharField(choices=[('loaned', 'loaned'), ('not_loaned', 'not_loaned')], default='no', max_length=20),
        ),
        migrations.AlterField(
            model_name='videoitemsmodel',
            name='loaned_date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='videoitemsmodel',
            name='release_date',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='videoitemsmodel',
            name='returned_at',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='videoitemsmodel',
            name='status',
            field=models.CharField(choices=[('loaned', 'loaned'), ('not_loaned', 'not_loaned')], default='no', max_length=20),
        ),
    ]
