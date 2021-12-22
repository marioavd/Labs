# Generated by Django 3.2.4 on 2021-12-04 14:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0007_auto_20211202_1732'),
        ('monitoring', '0032_alter_scheduledreview_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('state', models.CharField(blank=True, choices=[('A', 'Abierto'), ('C', 'CERRADO')], default='A', max_length=1, null=True)),
                ('comment', models.CharField(blank=True, max_length=200, null=True)),
                ('date_comment', models.DateTimeField()),
                ('email', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='monitoring.externuser')),
                ('pc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.workstation')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.DeleteModel(
            name='Report',
        ),
    ]