# Generated by Django 2.2 on 2020-06-17 04:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0004_auto_20200617_0411'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='permisos',
        ),
    ]
