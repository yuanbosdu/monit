# Generated by Django 2.0 on 2019-02-03 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0006_deviceruler'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deviceruler',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
