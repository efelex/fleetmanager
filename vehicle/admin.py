from django.contrib import admin
from .models import Vehicle, VehicleMake, VehicleModel, VehiclePoolType
# Register your models here.


class VehicleAdmin(admin.ModelAdmin):
    #fields = '__all__'
    list_display = ('registration_number', 'chassis_number', 'vehicle_model', 'color',
                    'date_created', 'last_service_date', 'vehicle_pool_type')


admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(VehicleModel)
admin.site.register(VehicleMake)
admin.site.register(VehiclePoolType)
