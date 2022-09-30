from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.middleware.csrf import get_token
from django.shortcuts import render

from teachers.forms import EditTeacherForm
from teachers.models import Teacher

from webargs.djangoparser import use_args
from webargs.fields import Str


@use_args(
    {
        'first_name': Str(required=False),
        'last_name': Str(required=False),
        'specialization': Str(required=False),
    },
    location='query'
)
def get_teachers(request, args):
    teachers = Teacher.objects.all()

    if len(args) != 0 and args.get('first_name') or args.get('last_name') or args.get('specialization'):
        teachers = teachers.filter(
            Q(first_name=args.get('first_name', '')) |
            Q(last_name=args.get('last_name', '')) |
            Q(specialization=args.get('specialization', ''))
        )
    return render(request, 'teachers/list.html', {'title': 'List of teachers', 'teachers': teachers})


def detail_teacher(request, teacher_id):
    teacher = Teacher.objects.get(pk=teacher_id)
    return render(request, 'teachers/detail.html', {'title': 'Teacher detail', 'teacher': teacher})


def update_teacher(request, teacher_id):
    teacher = Teacher.objects.get(pk=teacher_id)
    form = EditTeacherForm(request.POST or None, instance=teacher)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/teachers/')

    token = get_token(request)
    html_form = f'''
            <h1>Edit teacher || id {teacher_id}</h1><br><br>
            <form method="post">
            <input type="hidden" name="csrfmiddlewaretoken" value="{token}">
            <table>{form.as_table()}</table><br>
            <input type="submit" value="Submit"><br>
            </form>'''
    return HttpResponse(html_form)
