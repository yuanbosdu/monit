# Generated by Django 2.0 on 2019-01-14 13:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('zigbee', '0010_auto_20190114_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zigbee',
            name='uuid',
            field=models.UUIDField(blank=True, default=uuid.uuid1, null=True),
        ),
    ]