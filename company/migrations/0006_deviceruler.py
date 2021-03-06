# Generated by Django 2.0 on 2019-02-03 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_device_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceRuler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('ruler', models.CharField(max_length=100)),
                ('ctime', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rulers', to='company.Company')),
            ],
        ),
    ]
