from django.db import models
from django.utils import timezone
from vehicle.models import Vehicle, VehicleModel
from django.contrib.auth.models import User
# Create your models here.


class Fuel(models.Model):
    fuel = models.CharField(max_length=255)

    def __str__(self):
        return self.fuel


class RequisitionStatus(models.Model):
    requisition_status = models.CharField(max_length=255)

    def __str__(self):
        return self.requisition_status


class FuelRequistion(models.Model):
    requestor = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='requested_by')
    requstion_date = models.DateTimeField()
    approved_by = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, blank=True, null=True)
    approval_date = models.DateField(blank=True, null=True)
    fuel = models.ForeignKey(Fuel, on_delete=models.DO_NOTHING)
    fuel_recieved_by = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='recieved_by', blank=True, null=True)
    requisition_status = models.ForeignKey(
        RequisitionStatus, on_delete=models.CASCADE)
    amount_requested = models.DecimalField(max_digits=5, decimal_places=1)
    amount_approved = models.FloatField(blank=True, null=True)
    purpose = models.CharField(max_length=255)
    current_milage = models.FloatField()
    registration_number = models.ForeignKey(
        Vehicle, on_delete=models.DO_NOTHING)

    # class Meta:
    #     managed = True
    #     db_table = 'fuelrequistion'
    #     constraints = [
    # #         models.CheckConstraint(check=models.Q(
    # #             price__gte='0'), name='product_price_non_negative'),
    #     ]
