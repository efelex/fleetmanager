from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .forms import FuelRequistionForm
from .models import FuelRequisition
from .filters import RequisitionFilter
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
    # qs = self.model.objects.all()
    queryset = FuelRequisition.objects.select_related(
        'requestor__profile', 'approved_by', 'registration_number', 'fuel_recieved_by', 'fuel').filter(id=requisition_id)
    # print(queryset.query)
    requisition = get_object_or_404(queryset)
    print(requisition)
    context = {'requisition': requisition}
    return render(request,  "fuelmanagement/requistion_detail.html", context)


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
    # model = FuelRequisition
    # myfilter = RequisitionFilter()
    template_name = '/fuelmanagement/fuelrequisition_list.html'
    # context_object_name = 'fuelrequistions'
    # paginate_by = 4
    # ordering                        # how to order the vehicles by default

    def get_queryset(self):
        # qs = self.model.objects.all()
        qs = FuelRequisition.objects.select_related(
            'requestor__profile', 'approved_by', 'registration_number', 'fuel_recieved_by', 'fuel').all()
        requisition_filtered_list = RequisitionFilter(
            self.request.GET, queryset=qs)
        return requisition_filtered_list.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['requisition_filtered_list'] = RequisitionFilter(
            self.request.GET, queryset=self.get_queryset())
        # print(context.values)
        return context
