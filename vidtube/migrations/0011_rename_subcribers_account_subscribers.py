# Generated by Django 4.2.6 on 2024-01-09 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vidtube', '0010_subcribe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='subcribers',
            new_name='subscribers',
        ),
    ]
