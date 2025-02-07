# Generated by Django 3.2 on 2021-09-14 01:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='campus',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='campus',
            name='inactive_by',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='workstation',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='workstation',
            name='inactive_by',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='workstation',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.room'),
        ),
        migrations.AlterField(
            model_name='room',
            name='inactive_by',
            field=models.TextField(default=''),
        ),
    ]
