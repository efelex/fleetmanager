from django.db import models
from django.utils import timezone
# from fuelmanagement.models import VehicleModel
# import Fuel  fuelmanagement.models
# Create your models here.


class VehicleMake(models.Model):
    vehicle_make = models.CharField(max_length=255)

    def __str__(self):
        return self.vehicle_make


class VehicleModel(models.Model):

    vehicle_model = models.CharField(max_length=255)
    vehicle_make = models.ForeignKey(VehicleMake, on_delete=models.CASCADE)

    def __str__(self):
        return self.vehicle_model


class VehiclePoolType(models.Model):
    vehicle_pool_type = models.CharField(
        max_length=255, default="pool vehicle")

    def __str__(self):
        return self.vehicle_pool_type


class Vehicle(models.Model):

    registration_number = models.CharField(max_length=255)
    chassis_number = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    fuel = models.ForeignKey(
        "fuelmanagement.Fuel", on_delete=models.CASCADE, null=True)

    vehicle_model = models.ForeignKey(
        VehicleModel, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    last_service_date = models.DateField()
    vehicle_pool_type = models.ForeignKey(
        VehiclePoolType, on_delete=models.CASCADE)
    vehicle_model = models.ForeignKey(
        VehicleModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.registration_number
