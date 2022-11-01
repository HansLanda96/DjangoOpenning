from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView


from .forms import CreateTeacherForm, EditTeacherForm, TeacherFilterForm
from .models import Teacher


class CreateTeacherView(LoginRequiredMixin, CreateView):
    model = Teacher
    template_name = 'teachers/create.html'
    success_url = reverse_lazy('teachers:list')
    form_class = CreateTeacherForm


class DeleteTeacherView(LoginRequiredMixin, DeleteView):
    model = Teacher
    template_name = 'teachers/delete.html'
    success_url = reverse_lazy('teachers:list')


class DetailTeacherView(LoginRequiredMixin, DetailView):
    model = Teacher
    template_name = 'teachers/detail.html'


class ListTeacherView(ListView):
    model = Teacher
    template_name = 'teachers/list.html'

    def get_queryset(self):
        qs_list = Teacher.objects.all()
        filter_form = TeacherFilterForm(data=self.request.GET, queryset=qs_list)
        return filter_form


class UpdateTeacherView(LoginRequiredMixin, UpdateView):
    model = Teacher
    template_name = 'teachers/update.html'
    success_url = reverse_lazy('teachers:list')
    form_class = EditTeacherForm
