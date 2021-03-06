# Generated by Django 2.1 on 2020-05-10 20:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fuelmanagement', '0006_auto_20200510_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fuelrequistion',
            name='amount_approved',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fuelrequistion',
            name='approval_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fuelrequistion',
            name='approved_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='fuelrequistion',
            name='fuel_recieved_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='recieved_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='fuelrequistion',
            name='requestor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='requested_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
