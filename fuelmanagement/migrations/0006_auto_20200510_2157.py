# Generated by Django 2.1 on 2020-05-10 19:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fuelmanagement', '0005_auto_20200510_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fuelrequistion',
            name='approved_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
