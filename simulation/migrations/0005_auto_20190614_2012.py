# Generated by Django 2.2.2 on 2019-06-14 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulation', '0004_auto_20190614_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simulationmodel',
            name='mean_time',
            field=models.DecimalField(blank=True, decimal_places=5, default=0, max_digits=100, null=True),
        ),
        migrations.AlterField(
            model_name='simulationmodel',
            name='percent_trucks_in_queue',
            field=models.DecimalField(blank=True, decimal_places=5, default=0, max_digits=100, null=True),
        ),
    ]