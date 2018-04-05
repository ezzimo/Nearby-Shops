# Generated by Django 2.0.3 on 2018-04-05 05:48

from django.db import migrations
import django_google_maps.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shops_nearby', '0010_auto_20180405_0639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='geolocalisation',
            field=django_google_maps.fields.GeoLocationField(max_length=100, null=True),
        ),
    ]
