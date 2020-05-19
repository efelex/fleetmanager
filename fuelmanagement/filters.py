import django_filters
from .models import *


class RequisitionFilter(django_filters.FilterSet):
    class Meta:
        model = FuelRequisition
        # fields = '__all__'
        fields = ['requisition_status', 'requestor',
                  'requstion_date', 'fuel']

        # [
    # 'requstion_date',
    # 'approved_by',
    # 'approval_date',
    # 'fuel_recieved_by',
    # 'requisition_status',
    # 'amount_requested',
    # 'amount_approved',
    # 'purpose',
    # 'current_milage',
    # 'registration_number',
    # 'vehicle_model']
