# Generated by Django 2.2.1 on 2019-06-29 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20190621_0552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.SlugField(blank=True, default=1865537312, unique=True),
        ),
    ]
