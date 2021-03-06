# Generated by Django 2.2.2 on 2019-06-14 17:42

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulation', '0003_auto_20190614_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simulationmodel',
            name='n_trucks_in_queue',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None), blank=True, default=[[0]], null=True, size=None),
        ),
    ]
