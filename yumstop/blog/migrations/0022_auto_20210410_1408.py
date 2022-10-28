# Generated by Django 3.1.7 on 2021-04-10 08:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20210410_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointments',
            name='closing',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 10, 8, 38, 1, 974166, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='appointments',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 10, 8, 38, 1, 974166, tzinfo=utc)),
        ),
    ]