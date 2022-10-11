from django.db.models import Q # noqa
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from webargs.djangoparser import use_args # noqa
from webargs.fields import Str # noqa

from .forms import CreateGroupForm, GroupFilterForm, UpdateGroupForm
from .models import Group


def get_groups(request):
    groups = Group.objects.all()
    filter_form = GroupFilterForm(request.GET, queryset=groups)
    return render(request, 'groups/list.html', {'filter_form': filter_form})


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
