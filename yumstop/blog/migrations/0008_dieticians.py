# Generated by Django 3.1.7 on 2021-04-03 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210326_1346'),
    ]

    operations = [
        migrations.CreateModel(
            name='dieticians',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('qualifications', models.TextField()),
                ('ap', models.IntegerField()),
                ('blogs', models.IntegerField()),
                ('bookmark', models.CharField(default='Null', max_length=20)),
            ],
        ),
    ]