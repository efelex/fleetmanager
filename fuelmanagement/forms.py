from django import forms
from .models import FuelRequisition


class FuelRequistionForm(forms.ModelForm):

    class Meta:
        model = FuelRequisition
        fields = fields = '__all__'

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
