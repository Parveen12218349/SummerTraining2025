#from django.shortcuts import render
from django.views.generic import DetailView,UpdateView,DeleteView,ListView,CreateView
from .models import Portal
from django.urls import reverse_lazy
# Create your views here.

class PortalListView(ListView):
    model = Portal
    template_name = 'listall.html'
    context_object_name = 'portals'

class PortalDetailView(DetailView):
    model = Portal
    template_name = 'portaldetail.html'
    context_object_name = 'portal'

class PortalCreateView(CreateView):
    model = Portal
    template_name = 'createportal.html'
    context_object_name = 'portal'
    fields = '__all__'
    success_url = reverse_lazy('portal_list')

class PortalUpdateView(UpdateView):
    model = Portal
    template_name = 'editportal.html'
    context_object_name = 'portal'
    fields = '__all__'
    success_url = reverse_lazy('portal_list')

class PortalDeleteView(DeleteView):
    model = Portal
    template_name = 'deleteportal.html'
    context_object_name = 'portal'
    fields = '__all__'
    success_url = reverse_lazy('portal_list')

