# Generated by Django 2.2.12 on 2020-06-06 23:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('planfinder', '0004_auto_20200606_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighbourhoodplan',
            name='created_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
