from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.middleware.csrf import get_token
from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt

from webargs.djangoparser import use_args
from webargs.fields import Str

from .forms import CreateStudentForm, EditStudentForm
from .models import Student


def index(request):
    return HttpResponse('Welcome to LMS!')


@use_args(
    {
        'first_name': Str(required=False),
        'last_name': Str(required=False),
    },
    location='query'
)
def get_students(request, args):
    students = Student.objects.all()

    if len(args) != 0 and args.get('first_name') or args.get('last_name'):
        students = students.filter(
            Q(first_name=args.get('first_name', '')) |
            Q(last_name=args.get('last_name', ''))
        )
    return render(request, 'students/list.html', {'title': 'List of students', 'students': students})


def detail_student(request, student_id):
    student = Student.objects.get(pk=student_id)
    return render(request, 'students/detail.html', {'title': 'Student detail', 'student': student})


# @csrf_exempt allows to send POST request without CSRF token
def create_student(request):
    """CreateStudentForm"""
    if request.method == 'GET':
        form = CreateStudentForm()
    elif request.method == 'POST':
        form = CreateStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/students/')

    token = get_token(request)
    html_form = f'''
        <form method="post">
        <input type="hidden" name="csrfmiddlewaretoken" value="{token}">
        <table>{form.as_table()}</table>
        <input type="submit" value="Submit"><br>
        </form>'''

    return HttpResponse(html_form)


def edit_student(request, student_id):
    """EditStudentForm"""
    instance = Student.objects.get(pk=student_id)
    form = EditStudentForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/students/')

    token = get_token(request)
    html_form = f'''
        <h1>Edit student || id {student_id}</h1><br><br>
        <form method="post">
        <input type="hidden" name="csrfmiddlewaretoken" value="{token}">
        <table>{form.as_table()}</table>
        <input type="submit" value="Submit"><br>
        </form>'''

    return HttpResponse(html_form)
