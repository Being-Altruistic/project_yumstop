# Generated by Django 3.1.7 on 2021-04-16 12:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0036_auto_20210416_1147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointments',
            name='opening',
        ),
        migrations.AlterField(
            model_name='appointments',
            name='CLOSING',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 16, 12, 13, 4, 59386)),
        ),
    ]
