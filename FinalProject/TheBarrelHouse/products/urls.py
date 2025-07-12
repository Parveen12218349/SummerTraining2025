from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='products'),  # This resolves {% url 'products' %}
    path('add/', views.add_product, name='add_product'),
    path('my/', views.my_products, name='my_products'),
    path('edit/<int:pk>/', views.edit_product, name='edit_product'),
    path('delete/<int:pk>/', views.delete_product, name='delete_product'),
]
