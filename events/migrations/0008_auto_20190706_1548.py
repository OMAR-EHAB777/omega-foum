# Generated by Django 2.2.1 on 2019-07-06 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20190629_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.SlugField(blank=True, default=1880610592, unique=True),
        ),
    ]
