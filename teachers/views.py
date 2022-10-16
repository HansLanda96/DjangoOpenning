from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .forms import CreateTeacherForm, EditTeacherForm, TeacherFilterForm
from .models import Teacher


def get_teachers(request):
    teachers = Teacher.objects.all()
    filter_form = TeacherFilterForm(request.GET, queryset=teachers)
    return render(request, 'teachers/list.html', {'filter_form': filter_form})


def create_teacher(request):
    form = CreateTeacherForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('teachers:list'))
    return render(request, 'teachers/create.html', {'form': form})


def detail_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    return render(request, 'teachers/detail.html', {'teacher': teacher})


def update_teacher(request, teacher_id):
    instance = get_object_or_404(Teacher, pk=teacher_id)
    form = EditTeacherForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('teachers:list'))

    return render(request, 'teachers/update.html', {'form': form})


def delete_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    if request.method == 'POST':
        teacher.delete()
        return HttpResponseRedirect(reverse('teachers:list'))
    return render(request, 'teachers/delete.html', {'teacher': teacher})
