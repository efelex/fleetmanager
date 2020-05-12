from django import forms
from .models import FuelRequistion


class FuelRequistionForm(forms.ModelForm):

    class Meta:
        model = FuelRequistion
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
