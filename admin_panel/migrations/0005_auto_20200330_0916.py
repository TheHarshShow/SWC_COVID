# Generated by Django 3.0.3 on 2020-03-30 09:16

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0004_auto_20200328_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='request',
            name='city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='request',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(geography=True, srid=4326),
        ),
        migrations.AlterField(
            model_name='request',
            name='state',
            field=models.CharField(max_length=50),
        ),
    ]
