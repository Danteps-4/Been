# Generated by Django 5.1.2 on 2024-10-26 03:30

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_country_continent'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='landscape',
            field=models.ImageField(default='landscapes/default.jpg', upload_to=core.models.user_directory_path_landscape),
        ),
    ]