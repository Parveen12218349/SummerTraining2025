#from django.shortcuts import render
from django.views.generic import DetailView,UpdateView,DeleteView,ListView,CreateView
from .models import Catalog
from django.urls import reverse_lazy
# Create your views here.

class CatalogListView(ListView):
    model = Catalog
    template_name = 'listall.html'
    context_object_name = 'catalogs'

class CatalogDetailView(DetailView):
    model = Catalog
    template_name = 'catalogdetail.html'
    context_object_name = 'catalog'

class CatalogCreateView(CreateView):
    model = Catalog
    template_name = 'createcatalog.html'
    context_object_name = 'catalog'
    fields = '__all__'
    success_url = reverse_lazy('product_list')

class CatalogUpdateView(UpdateView):
    model = Catalog
    template_name = 'editcatalog.html'
    context_object_name = 'catalog'
    fields = '__all__'
    success_url = reverse_lazy('product_list')

class CatalogDeleteView(DeleteView):
    model = Catalog
    template_name = 'deletecatalog.html'
    context_object_name = 'catalog'
    fields = '__all__'
    success_url = reverse_lazy('product_list')

