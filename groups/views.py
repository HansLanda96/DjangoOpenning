from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from webargs.djangoparser import use_args
from webargs.fields import Str

from .forms import CreateGroupForm, UpdateGroupForm
from .models import Group


@use_args(
    {
        'name': Str(required=False),
        'start_date': Str(required=False),
    },
    location='query'
)
def get_groups(request, args):
    groups = Group.objects.all()
    if len(args) != 0 and args.get('name') or args.get('start_date'):
        groups = groups.filter(
            Q(name=args.get('name', '')) |
            Q(start_date=args.get('start_date', 'start_date'))
        )
    return render(request, 'groups/list.html', {'groups': groups})


def detail_group(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    return render(request, 'groups/detail.html', {'group': group})


def create_group(request):
    form = CreateGroupForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('groups:list'))
    return render(request, 'groups/create.html', {'form': form})


def update_group(request, group_id):
    instance = get_object_or_404(Group, pk=group_id)
    form = UpdateGroupForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('groups:list'))
    return render(request, 'groups/update.html', {'form': form})


def delete_group(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    if request.method == 'POST':
        group.delete()
        return HttpResponseRedirect(reverse('groups:list'))
    return render(request, 'groups/delete.html', {'group': group})
