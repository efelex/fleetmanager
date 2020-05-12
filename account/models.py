from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Department(models.Model):
    department_name = models.CharField(max_length=255)

    def __str__(self):
        return self.department_name


class Station(models.Model):
    station_name = models.CharField(max_length=255)

    def __str__(self):
        return self.station_name


class OfficerDesignation(models.Model):
    officer_title = models.CharField(max_length=255)

    def __str__(self):
        return self.officer_title


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    employee_number = models.CharField(max_length=255)
    national_identity_number = models.CharField(max_length=255)
    sex = models.CharField(max_length=1, default="M")
    driver_license_number = models.CharField(max_length=255, null=True)
    driver_license_class = models.CharField(max_length=255, null=True)
    competence_certificate_number = models.CharField(max_length=255, null=True)
    department_name = models.ForeignKey(
        Department, on_delete=models.SET_NULL, null=True)
    station_name = models.ForeignKey(
        Station, on_delete=models.SET_NULL, null=True)
    officer_title = models.ForeignKey(
        OfficerDesignation, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user.username
