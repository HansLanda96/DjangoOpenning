from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .forms import GroupCreateForm, GroupFilterForm, GroupUpdateForm
from .models import Group


def create_group(request):
    if request.method == 'POST':
        form = GroupCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))
    form = GroupCreateForm()
    return render(request, 'groups/create.html', {'form': form})


def delete_group(request, group_id):
    return HttpResponse('Group delete view.')


def detail_group(request, group_id):
    return HttpResponse('Group detail view.')


def get_groups(request):
    groups = Group.objects.all()
    filter_form = GroupFilterForm(request.GET, queryset=groups)
    return render(request, 'groups/list.html', {'groups': groups, 'filter_form': filter_form})


def update_group(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    if request.method == 'POST':
        form = GroupUpdateForm(instance=group, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))
    form = GroupUpdateForm(instance=group)
    return render(request, 'groups/update.html', {'form': form, 'group': group})
