# Generated by Django 4.2.6 on 2024-01-07 08:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vidtube', '0008_alter_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='dat',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
