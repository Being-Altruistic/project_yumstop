# Generated by Django 3.1.7 on 2021-04-10 13:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0033_auto_20210410_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='CLOSING',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 10, 13, 25, 25, 993421, tzinfo=utc)),
        ),
    ]