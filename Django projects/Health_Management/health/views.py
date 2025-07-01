#from django.shortcuts import render
from django.views.generic import DetailView,UpdateView,DeleteView,ListView,CreateView
from .models import Health
from django.urls import reverse_lazy
# Create your views here.

class HealthListView(ListView):
    model = Health
    template_name = 'listall.html'
    context_object_name = 'healths'

class HealthDetailView(DetailView):
    model = Health
    template_name = 'datadetail.html'
    context_object_name = 'health'

class HealthCreateView(CreateView):
    model = Health
    template_name = 'createdata.html'
    fields = '__all__'
    success_url = reverse_lazy('patient_list')

class HealthUpdateView(UpdateView):
    model = Health
    template_name = 'editdata.html'
    fields = '__all__'
    success_url = reverse_lazy('patient_list')

class HealthDeleteView(DeleteView):
    model = Health
    template_name = 'deletedata.html'
    fields = '__all__'
    success_url = reverse_lazy('patient_list')

