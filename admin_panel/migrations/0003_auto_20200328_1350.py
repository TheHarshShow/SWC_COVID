# Generated by Django 3.0.3 on 2020-03-28 13:50

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0002_auto_20200328_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(geography=True, null=True, srid=4326),
        ),
    ]
