# Generated by Django 2.1.1 on 2018-10-04 08:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cbv', '0011_auto_20180927_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 4, 8, 5, 58, 50069, tzinfo=utc)),
        ),
    ]
