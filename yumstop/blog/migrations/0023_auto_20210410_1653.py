# Generated by Django 3.1.7 on 2021-04-10 11:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_auto_20210410_1408'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointments',
            name='closing',
        ),
        migrations.RemoveField(
            model_name='appointments',
            name='date',
        ),
        migrations.AddField(
            model_name='appointments',
            name='CLOSING',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 10, 11, 23, 5, 49584, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='appointments',
            name='request_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 10, 11, 23, 5, 49584, tzinfo=utc)),
        ),
    ]
