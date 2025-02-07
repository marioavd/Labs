# Generated by Django 3.2 on 2021-11-11 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('licenses', '0006_software_form_software_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeLicense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.TextField(default='Open source')),
                ('description', models.TextField(default='')),
            ],
        ),
        migrations.AlterField(
            model_name='softwareform',
            name='software_type',
            field=models.IntegerField(choices=[(1, 'Open Source'), (4, 'Estatica'), (5, 'Flotante'), (6, 'Fisica')], default=1),
        ),
        migrations.AlterField(
            model_name='licenseslist',
            name='license_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='licenses.typelicense'),
        ),
    ]
