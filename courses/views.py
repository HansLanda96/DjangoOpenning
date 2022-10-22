from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView


from .forms import CourseCreateForm, CourseFilterForm, CourseUpdateForm
from .models import Course


class CreateCourseView(CreateView, LoginRequiredMixin):
    model = Course
    template_name = 'courses/create.html'
    success_url = reverse_lazy('courses:list')
    form_class = CourseCreateForm


class DeleteCourseView(DeleteView, LoginRequiredMixin):
    model = Course
    template_name = 'courses/delete.html'
    success_url = reverse_lazy('courses:list')


class DetailCourseView(DetailView, LoginRequiredMixin):
    model = Course
    template_name = 'courses/detail.html'


class ListCourseView(ListView):
    model = Course
    template_name = 'courses/list.html'

    def get_queryset(self):
        courses = Course.objects.select_related('course_group')
        filter_form = CourseFilterForm(data=self.request.GET, queryset=courses)
        return filter_form


class UpdateCourseView(UpdateView, LoginRequiredMixin):
    model = Course
    template_name = 'courses/update.html'
    success_url = reverse_lazy('courses:list')
    form_class = CourseUpdateForm
