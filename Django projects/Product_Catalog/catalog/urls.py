from django.urls import path
#from catalog import views
from .views import (
    CatalogListView,
    CatalogCreateView,
    CatalogDeleteView,
    CatalogDetailView,
    CatalogUpdateView
)



urlpatterns = [
    path('', CatalogListView.as_view(), name='product_list'),
    path('<int:pk>/', CatalogDetailView.as_view(), name='product_detail'),
    path('add/', CatalogCreateView.as_view(), name='product_add'),
    path('modify/<int:pk>/', CatalogUpdateView.as_view(), name='product_edit'),
    path('delete/<int:pk>/', CatalogDeleteView.as_view(), name='product_delete'),
]
