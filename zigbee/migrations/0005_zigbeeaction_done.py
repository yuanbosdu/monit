# Generated by Django 2.0 on 2018-10-26 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zigbee', '0004_auto_20181025_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='zigbeeaction',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
