# Generated by Django 4.2.6 on 2024-01-03 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vidtube', '0004_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumb',
            field=models.ImageField(default='C:\\Users\\sures\\OneDrive\\Documents\\python\\django\\youtube_clone\\static\\images\\thumbnail1.png', upload_to='C:\\Users\\sures\\OneDrive\\Documents\\python\\django\\youtube_clone\\static\\images'),
        ),
    ]
