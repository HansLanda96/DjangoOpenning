from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from students.models import Student

from .forms import GroupCreateForm, GroupUpdateForm
from .models import Group


class CreateGroupView(CreateView):  # Not working properly yet. Teacher issue. SQL issue.
    model = Group
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/create.html'
    form_class = GroupCreateForm

    def form_valid(self, form):
        response = super().form_valid(form)
        group = form.save()
        students = form.cleaned_data['students']
        for student in students:
            student.group = group
            student.save()
        return response


class DeleteGroupView(DeleteView):
    model = Group
    template_name = 'groups/delete.html'
    success_url = reverse_lazy('groups:list')


class DetailGroupView(DetailView):
    model = Group
    template_name = 'groups/detail.html'


class ListGroupView(ListView):
    model = Group
    template_name = 'groups/list.html'


class UpdateGroupView(UpdateView):
    model = Group
    form_class = GroupUpdateForm
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = self.get_object().students.prefetch_related('headman_group')
        return context

    def get_initial(self):
        initial = super().get_initial()
        try:
            initial['headman_field'] = self.object.headman.pk
        except AttributeError:
            initial['headman_field'] = 0
        return initial

    def form_valid(self, form):
        response = super().form_valid(form)
        pk = int(form.cleaned_data['headman_field'])
        if pk:
            form.instance.headman = Student.objects.get(pk=pk)
        else:
            form.instance.headman = None
        form.save()
        return response


# def create_group(request):
#     if request.method == 'POST':
#         form = GroupCreateForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('groups:list'))
#     form = GroupCreateForm()
#     return render(request, 'groups/create.html', {'form': form})

# optional to ListView
# def get_groups(request):
#     groups = Group.objects.all()
#     filter_form = GroupFilterForm(request.GET, queryset=groups)
#     return render(request, 'groups/list.html', {'groups': groups, 'filter_form': filter_form})


# Optional update group view. Withot generic classes.
# def update_group(request, group_id):
#     group = get_object_or_404(Group, pk=group_id)
#     if request.method == 'POST':
#         form = GroupUpdateForm(instance=group, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('groups:list'))
#     form = GroupUpdateForm(instance=group)
#     return render(
#         request,
#         'groups/update.html',
#         {
#             'form': form,
#             'students': group.students.prefetch_related('headman_group')
#         }
#     )
