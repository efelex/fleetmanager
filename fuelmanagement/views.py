from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .forms import FuelRequistionForm
from .models import FuelRequisition
from django.views.generic import DetailView, ListView


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


def fuelrequistion_detail_view(request, requisition_id):
    # return HttpResponse(requisition_id)
    requisition = FuelRequisition.objects.get(id=requisition_id)
    print(requisition)
    context = {'requisition': requisition}
    return render(request,  "fuelmanagement/fuelrequisition_detail.html", context)


# #********************************8
# class FuelRequistionDetailView(DetailView):
#     # model = FuelRequistion
#     queryset = FuelRequistion.objects.all()
#     # 'url {'viewrequistiondetail'}'
#     template_name = '/fuelmanagement/fuelrequisition_detail.html  '
#     context_object_name = 'fuelrequisitions'

#     def get_object(self):
#         id_ = self.kwargs.get("id")
#         return get_object_or_404(FuelRequistion, id=id_)


class FuelRequistionListView(ListView):
    model = FuelRequisition
    template_name = '/fuelmanagement/fuelrequisition_list.html'
    context_object_name = 'fuelrequisitions'
    # ordering                        # how to order the vehicles by default
