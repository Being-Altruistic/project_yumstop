# Generated by Django 3.1.7 on 2021-04-10 13:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0029_auto_20210410_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='CLOSING',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]