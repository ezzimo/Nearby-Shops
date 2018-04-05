# Generated by Django 2.0.3 on 2018-04-05 05:29

from django.db import migrations
import django_google_maps.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shops_nearby', '0007_auto_20180405_0613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='geolocalisation',
            field=django_google_maps.fields.GeoLocationField(default=(34.0132484, -6.83255), max_length=100),
        ),
    ]
