# Generated by Django 3.2.6 on 2021-09-26 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SoftwareRequestModel',
            fields=[
                ('id_request', models.AutoField(primary_key=True, serialize=False)),
                ('creation_date', models.DateField(auto_now=True, verbose_name='Creation date')),
                ('name_user', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('rut', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=100)),
                ('nrc', models.CharField(max_length=8)),
                ('software_name', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=330)),
            ],
            options={
                'verbose_name': 'solicitud',
                'verbose_name_plural': 'solicitudes',
            },
        ),
    ]
