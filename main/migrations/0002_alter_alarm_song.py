# Generated by Django 5.1.3 on 2024-11-07 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alarm',
            name='song',
            field=models.FileField(default="{%static 'Godzila'%}", upload_to=''),
        ),
    ]
