from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from .forms import FuelRequistionForm
from .models import FuelRequistion
from django.views.generic import ListView


def index(request):
    return HttpResponse("hello world welcome to fuel management")


def fuelrequisition_create_view(request):
    form = FuelRequistionForm(request.POST or None)
    if request.method == 'POST':
        form = FuelRequistionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, ('Fuel Requistion submited  successfully '))

        # Redirect to a success page.
           # return redirect('/')
    else:
        messages.success(
            request, ('Failed to create Fuel Requistion! You have some errors .... please try again'))
        # return redirect('vehicle_create')
    context = {

        'form': form}
    # obj = VehicleMake.objects.get(id=3)

    return render(request,  "fuelmanagement/create_requistion.html", context)


class FuelRequistionListView(ListView):

    model = FuelRequistion
    template_name = '/fuelmanagement/fuelrequisition_list.html'
    context_object_name = 'fuelrequisitions'
    # ordering                        # how to order the vehicles by default
