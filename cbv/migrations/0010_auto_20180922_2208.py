# Generated by Django 2.1.1 on 2018-09-22 17:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cbv', '0009_auto_20180922_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 22, 17, 8, 51, 380793, tzinfo=utc)),
        ),
    ]
