from django.urls import path
from . import views

urlpatterns = [
    path('place/<int:product_id>/', views.place_order, name='place_order'),
]

