# Generated by Django 2.0.7 on 2018-09-18 07:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 18, 7, 35, 31, 594305, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(default='UN4VlLu7', max_length=8),
        ),
    ]
