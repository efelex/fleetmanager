from django.contrib import admin
# Register your models here.
from .models import Fuel, RequisitionStatus, FuelRequisition
from vehicle.models import VehicleModel


class FuelRequistionAdmin(admin.ModelAdmin):
    #fields = '__all__'
    list_display = (
        'requestor',
        'registration_number',
        'purpose',
        'requstion_date',
        'fuel',
        'approved_by',
        'approval_date',
        'fuel_recieved_by',
        'requisition_status',
        'amount_requested',
        'amount_approved',
        'current_milage'


    )


admin.site.register(Fuel)
admin.site.register(RequisitionStatus)
admin.site.register(FuelRequisition, FuelRequistionAdmin)
