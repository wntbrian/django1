# Generated by Django 2.0.1 on 2018-01-18 08:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20180117_0403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='data',
        ),
        migrations.AddField(
            model_name='album',
            name='data',
            field=models.DateField(blank=True, default=django.utils.timezone.now, verbose_name='дата выхода'),
        ),
    ]
