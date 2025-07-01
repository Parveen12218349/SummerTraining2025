from django.urls import path
#from catalog import views
from .views import (
    CourseListView,
    CourseCreateView,
    CourseDeleteView,
    CourseDetailView,
    CourseUpdateView
)



urlpatterns = [
    path('', CourseListView.as_view(), name='course_list'),
    path('<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('add/', CourseCreateView.as_view(), name='course_add'),
    path('modify/<int:pk>/', CourseUpdateView.as_view(), name='course_edit'),
    path('delete/<int:pk>/', CourseDeleteView.as_view(), name='course_delete'),
]
