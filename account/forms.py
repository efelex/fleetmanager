from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
from django import forms

# class UserCreationForm


class UserCreatForm(UserCreationForm):
    email = forms.EmailField(max_length=100, required=False)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('employee_number', 'sex', 'driver_license_number', 'driver_license_class', 'station_name',
                  'national_identity_number', 'department_name', 'officer_title')
