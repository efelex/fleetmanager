from django.forms import ModelForm
from .models import VehicleMake, Vehicle


class VehicleMekeForm(ModelForm):
    class Meta:
        model = VehicleMake
        fields = ['vehicle_make']


class VehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = ['registration_number', 'chassis_number', 'vehicle_model', 'color',
                  'date_created', 'last_service_date', 'vehicle_pool_type']
