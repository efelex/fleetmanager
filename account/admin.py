from django.contrib import admin
from .models import UserProfile, Department, Station, OfficerDesignation
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Department)
admin.site.register(Station)
admin.site.register(OfficerDesignation)
