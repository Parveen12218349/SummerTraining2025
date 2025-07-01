from django.urls import path
from .views import(
    HealthListView,
    HealthCreateView,
    HealthDeleteView,
    HealthDetailView,
    HealthUpdateView
)

urlpatterns = [
    path('', HealthListView.as_view(), name='patient_list'),
    path('add/', HealthCreateView.as_view(), name='patient_create'),
    path('<int:pk>/', HealthDetailView.as_view(), name='patient_detail'),
    path('modify/<int:pk>/', HealthUpdateView.as_view(), name='patient_edit'),
    path('delete/<int:pk>/', HealthDeleteView.as_view(), name='patient_delete'),
]