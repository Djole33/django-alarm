# Generated by Django 5.1.3 on 2024-11-08 11:06

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_timer_delete_alarm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timer',
            name='start_time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
