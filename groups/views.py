from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.middleware.csrf import get_token
from django.shortcuts import render


from webargs.djangoparser import use_args
from webargs.fields import Str

from .forms import UpdateGroupForm
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
            Q(start_date=args.get('start_date', ''))
        )
    return render(request, 'groups/list.html', {'title': 'List of groups', 'groups': groups})


def detail_group(request, group_id):
    group = Group.objects.get(pk=group_id)
    return render(request, 'groups/detail.html', {'title': 'Group detail', 'group': group})


def update_group(request, group_id):
    group = Group.objects.get(pk=group_id)
    form = UpdateGroupForm(request.POST or None, instance=group)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/teachers/')

    token = get_token(request)
    html_form = f'''
                <h1>Edit teacher || id {group_id}</h1><br><br>
                <form method="post">
                <input type="hidden" name="csrfmiddlewaretoken" value="{token}">
                <table>{form.as_table()}</table><br>
                <input type="submit" value="Submit"><br>
                </form>'''
    return HttpResponse(html_form)
