# Generated by Django 5.1.5 on 2025-01-31 16:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='stroy/uploads/images')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='story', to='person.person')),
            ],
        ),
    ]
