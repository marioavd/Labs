# Generated by Django 3.2.4 on 2021-11-05 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0025_delete_pc_maintenance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduledreview',
            name='date_scheduled',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='scheduledreview',
            name='room',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
