# Generated by Django 3.1.7 on 2021-04-10 11:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_auto_20210410_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='CLOSING',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 10, 11, 32, 12, 601518, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='appointments',
            name='request_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
