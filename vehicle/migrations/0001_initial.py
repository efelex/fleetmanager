# Generated by Django 2.1 on 2020-04-25 19:10

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fuelmanagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_number', models.CharField(max_length=255)),
                ('chassis_number', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_service_date', models.DateField()),
                ('fuel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fuelmanagement.Fuel')),
            ],
        ),
        migrations.CreateModel(
            name='VehicleMake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_make', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_model', models.CharField(max_length=255)),
                ('vehicle_make', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.VehicleMake')),
            ],
        ),
        migrations.CreateModel(
            name='VehiclePoolType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_pool_type', models.CharField(default='pool vehicle', max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='vehicle',
            name='vehicle_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.VehicleModel'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='vehicle_pool_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.VehiclePoolType'),
        ),
    ]
