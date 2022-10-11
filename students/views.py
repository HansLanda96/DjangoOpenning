from django.db.models import Q  # noqa
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from webargs.djangoparser import use_args   # noqa
from webargs.fields import Str  # noqa

from .forms import CreateStudentForm, EditStudentForm, StudentFilterForm
from .models import Student


# @use_args(
#     {
#         'first_name': Str(required=False),
#         'last_name': Str(required=False),
#     },
#     location='query'
# )
def get_students(request):
    students = Student.objects.all()
    filter_form = StudentFilterForm(data=request.GET, queryset=students)
    return render(request, 'students/list.html', context={'filter_form': filter_form})

    # if len(args) != 0 and args.get('first_name') or args.get('last_name'):
    #     students = students.filter(
    #         Q(first_name=args.get('first_name', '').title()) |
    #         Q(last_name=args.get('last_name', '').title())
    #     )
    # return render(request, 'students/list.html', {'title': 'List of students', 'students': students})


def detail_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'students/detail.html', {'title': 'Student detail', 'student': student})


def create_student(request):
    """CreateStudentForm"""
    if request.method == 'GET':
        form = CreateStudentForm()
    elif request.method == 'POST':
        form = CreateStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:list'))
    return render(request, 'students/create.html', {'title': 'Create student', 'form': form})


def edit_student(request, student_id):
    """EditStudentForm"""
    instance = get_object_or_404(Student, pk=student_id)
    form = EditStudentForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('students:list'))

    return render(request, 'students/update.html', {'title': 'Edit student', 'form': form})


def delete_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        student.delete()
        return HttpResponseRedirect(reverse('students:list'))
    return render(request, 'students/delete.html', {'student': student})
