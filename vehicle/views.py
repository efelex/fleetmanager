from django.shortcuts import render, redirect

# Create your views here.
from .models import VehicleMake, Vehicle
from django.contrib import messages
from .forms import VehicleMekeForm, VehicleForm

from django.views.generic import ListView
# Create your views here.


def vehicle_make_view(request):
    obj = VehicleMake.objects.all()
    context = {'vehicle_makes': obj}
    return render(request,  "vehicle/vehicleMake.html", context)


def vehicle_make_create_view(request):
    form = VehicleMekeForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {

        'form': form}
    # obj = VehicleMake.objects.get(id=3)

    return render(request,  "vehicle/vehicleMake_create.html", context)


def vehicle_create_view(request):
    form = VehicleForm(request.POST or None)
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('Vehicle created successfully '))

        # Redirect to a success page.
           # return redirect('/')
    else:
        messages.success(
            request, ('Failed to create vehicle! You have some errors .... please try again'))
        # return redirect('vehicle_create')
    context = {

        'form': form}
    # obj = VehicleMake.objects.get(id=3)

    return render(request,  "vehicle/vehicle_create.html", context)


# def vehicle_list_view(request):
#     obj = Vehicle.objects.all()
#     context = {'vehicles': obj}
#     return render(request,  "vehicle/vehicleMake.html", context)


class VehicleListView(ListView):

    model = Vehicle
    template_name = '/vehicle/vehicle_list.html'
    context_object_name = 'vehicles'
    # ordering                        # how to order the vehicles by default
