# Generated by Django 2.0.3 on 2018-03-25 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops_nearby', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='preferred',
            field=models.ManyToManyField(related_name='Preferred', to='shops_nearby.Shop'),
        ),
    ]