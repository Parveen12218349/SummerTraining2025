from django.shortcuts import render
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from .models import Course
from django.urls import reverse_lazy
# Create your views here.

class CourseListView(ListView):
    model = Course
    template_name = 'courselist.html'
    context_object_name = 'courses'

class CourseDetailView(DetailView):
    model = Course
    template_name = 'coursedetail.html'
    context_object_name = 'course'

class CourseCreateView(CreateView):
    model = Course
    template_name = 'createcourse.html'
    fields = '__all__'
    success_url = reverse_lazy('course_list')

class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'editcourse.html'
    fields = '__all__'
    success_url = reverse_lazy('course_list')

class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'deletecourse.html'
    fields = '__all__'
    success_url = reverse_lazy('course_list')

