# Generated by Django 5.1.5 on 2025-02-03 15:01

import video.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0002_video_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='video/uploads/thumbnails/'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(upload_to='video/uploads/videos/', validators=[video.models.validate_video_file]),
        ),
    ]
