# Generated by Django 2.1 on 2020-05-04 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fuelmanagement', '0003_auto_20200504_2358'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fuelrequistion',
            old_name='recieved_by',
            new_name='fuel_recieved_by',
        ),
    ]
