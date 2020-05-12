"""rtsafleet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from pages.views import home_view, about_view
from vehicle.views import vehicle_make_view, vehicle_make_create_view, vehicle_create_view, VehicleListView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('fuelmanagement/', include('fuelmanagement.urls')),
    path('account/', include('account.urls')),
    path('', home_view, name='home_view'),
    path('home/', home_view, name='home_view'),
    path('about/', about_view, name='about_view'),
    path('', home_view, name='home_view'),
    path('vehicleMake/', vehicle_make_view, name='vehicle_make_view'),
    path('vehicle/create/', vehicle_create_view, name='vehicle_create'),
    path('vehicle/VehicleMakeCreate/', vehicle_make_create_view,
         name='vehicle_make_create_view'),
    path('vehicle/list', VehicleListView.as_view(), name='vehiclelist'),
    #path('vehicle/VehicleMakeCreate/',vehicle_make_create_view, name='vehicle_make_create_view'),

    # vehicle/vehicle_list html
]
