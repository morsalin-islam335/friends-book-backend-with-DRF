# Generated by Django 5.1.5 on 2025-01-31 18:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('person', '0001_initial'),
        ('story', '0002_story_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Replay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=700)),
                ('image', models.ImageField(upload_to='replay/uploads/image')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='replay.replay')),
                ('replayer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='story_replaies', to='person.person')),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replaies', to='story.story')),
            ],
        ),
    ]
