# Generated by Django 2.1 on 2020-05-10 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fuelmanagement', '0009_fuelrequistion_requstion_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='fuelrequistion',
            name='fuel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='fuelmanagement.Fuel'),
            preserve_default=False,
        ),
    ]
