# Generated by Django 2.2.1 on 2019-06-29 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20190629_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.SlugField(blank=True, default=1865537312, unique=True),
        ),
    ]
