# Generated by Django 3.2.4 on 2021-09-26 22:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0012_alter_report_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='report',
            options={'ordering': ['date_created']},
        ),
    ]
