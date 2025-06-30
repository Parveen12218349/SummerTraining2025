from django.urls import path
from .views import(
    PortalListView,
    PortalCreateView,
    PortalDeleteView,
    PortalDetailView,
    PortalUpdateView
)

urlpatterns = [
    path('', PortalListView.as_view(), name='portal-list'),
    path('add/', PortalCreateView.as_view(), name='portal-create'),
    path('<int:pk>/', PortalDetailView.as_view(), name='portal-detail'),
    path('modify/<int:pk>/', PortalUpdateView.as_view(), name='portal-update'),
    path('delete/<int:pk>/', PortalDeleteView.as_view(), name='portal-delete'),
]