# Generated by Django 3.1.7 on 2021-04-09 19:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_appointments_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='date',
            field=models.DateTimeField(default=datetime.date(2021, 4, 10)),
        ),
    ]
