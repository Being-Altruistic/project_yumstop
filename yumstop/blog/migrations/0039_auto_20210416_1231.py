# Generated by Django 3.1.7 on 2021-04-16 12:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0038_auto_20210416_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointments',
            name='patient_certificate',
            field=models.TextField(default='Null', max_length=300),
        ),
        migrations.AlterField(
            model_name='appointments',
            name='CLOSING',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 16, 12, 31, 22, 686383)),
        ),
    ]
