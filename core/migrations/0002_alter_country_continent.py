# Generated by Django 5.1.2 on 2024-10-22 17:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='continent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='countries', to='core.continent'),
        ),
    ]
