from django.urls import path
from .views import fuelrequisition_create_view, index, FuelRequistionListView, fuelrequistion_detail_view
# , FuelRequistionDetailView
urlpatterns = [
    path('', index, name='index'),
    path('fuelrequisition/', fuelrequisition_create_view, name='fuelrequisition'),
    path('fuelrequisition/list', FuelRequistionListView.as_view(),
         name='fuelrequisitionlist'),
    path('fuelrequisition/<int:requisition_id>', fuelrequistion_detail_view,
         name='viewrequistiondetail'),
    # path('fuelrequisition/<int:id>', FuelRequistionDetailView.as_view(),
    #      name='viewrequistiondetail'),

]
