# Generated by Django 2.0.7 on 2018-09-15 18:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cbv', '0002_auto_20180915_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 15, 18, 25, 47, 142658, tzinfo=utc)),
        ),
    ]
