# Generated by Django 3.2.4 on 2021-10-22 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0022_auto_20211022_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='externuser',
            name='email',
            field=models.EmailField(max_length=60, unique=True),
        ),
    ]
