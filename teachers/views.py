from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from teachers.forms import CreateTeacherForm, EditTeacherForm
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
            Q(first_name=args.get('first_name', '').title()) |
            Q(last_name=args.get('last_name', '').title()) |
            Q(specialization=args.get('specialization', '').lower())
        )
    return render(request, 'teachers/list.html', {'teachers': teachers})


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
