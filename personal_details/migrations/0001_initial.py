<<<<<<< HEAD
# Generated by Django 5.1.5 on 2025-01-30 00:37

import django.db.models.deletion
=======
# Generated by Django 5.1.5 on 2025-01-29 15:08

>>>>>>> 39b37c98d3bc9c24d5cf7d24db19d899ee982453
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
<<<<<<< HEAD
        ('person', '0001_initial'),
=======
>>>>>>> 39b37c98d3bc9c24d5cf7d24db19d899ee982453
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('profession', models.CharField(blank=True, max_length=40, null=True)),
                ('dateOfBirth', models.DateField(verbose_name='date of birth')),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='person.person')),
=======
                ('profession', models.TextField(blank=True, max_length=40, null=True)),
                ('dateOfBirth', models.DateField()),
>>>>>>> 39b37c98d3bc9c24d5cf7d24db19d899ee982453
            ],
        ),
    ]
