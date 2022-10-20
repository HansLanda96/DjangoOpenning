from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import CreateStudentForm, StudentFilterForm, UpdateStudentForm
from .models import Student


class CreateStudentView(CreateView):
    model = Student
    template_name = 'students/create.html'
    success_url = reverse_lazy('students:list')
    form_class = CreateStudentForm


class DeleteStudentView(DeleteView):
    model = Student
    template_name = 'students/delete.html'
    success_url = reverse_lazy('students:list')


class DetailStudentView(DetailView):
    model = Student
    template_name = 'students/detail.html'


class ListStudentView(ListView):
    model = Student
    template_name = 'students/list.html'
    # queryset = Student.objects.select_related('group')

    def get_queryset(self):
        students = Student.objects.select_related('group')
        filter_form = StudentFilterForm(data=self.request.GET, queryset=students)
        return filter_form


@login_required
def detail_student(request, student_id):
    student = Student.objects.get(pk=student_id)
    return render(request, 'students/detail.html', {'student': student})


@login_required
def create_student(request):
    if request.method == 'POST':
        form = CreateStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:list'))
        form = CreateStudentForm()
        return render(request, 'students/create.html', {'form': form})


class UpdateStudentView(UpdateView, LoginRequiredMixin):
    model = Student
    template_name = 'students/update.html'
    success_url = reverse_lazy('students:list')
    form_class = UpdateStudentForm


@login_required
def delete_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        student.delete()
        return HttpResponseRedirect(reverse('students:list'))
    return render(request, 'students/delete.html', {'student': student})
