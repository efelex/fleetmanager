# Generated by Django 2.1 on 2020-05-12 14:37

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fuelmanagement', '0010_fuelrequistion_fuel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FuelRequistion',
            new_name='FuelRequisition',
        ),
    ]
