from django.urls import path
from .views import fuelrequisition_create_view, index, FuelRequistionListView
urlpatterns = [
    path('', index, name='index'),
    path('fuelrequisition/', fuelrequisition_create_view, name='fuelrequisition'),
    path('fuelrequisition/list', FuelRequistionListView.as_view(),
         name='fuelrequisitionlist'),
]
