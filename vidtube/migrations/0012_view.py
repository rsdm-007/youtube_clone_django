# Generated by Django 4.2.6 on 2024-05-21 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vidtube', '0011_rename_subcribers_account_subscribers'),
    ]

    operations = [
        migrations.CreateModel(
            name='view',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('vid_id', models.CharField(max_length=150)),
            ],
        ),
    ]
