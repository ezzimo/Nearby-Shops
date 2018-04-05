# Generated by Django 2.0.3 on 2018-04-03 03:16

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops_nearby', '0003_auto_20180327_0754'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='disliked',
            field=models.ManyToManyField(related_name='Disliked', to='shops_nearby.Shop'),
        ),
    ]
