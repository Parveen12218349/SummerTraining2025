from django.urls import path

from booksmgnt import views

urlpatterns = [
    path('',views.book_list,name='book_list'),
]