# Generated by Django 2.0 on 2019-01-14 06:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('zigbee', '0009_auto_20190103_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zigbee',
            name='uuid',
            field=models.UUIDField(blank=True, default=uuid.UUID('6c8630ba-17c7-11e9-98e5-fcaa14cc1e81'), null=True),
        ),
    ]