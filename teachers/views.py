from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView


from .forms import CreateTeacherForm, EditTeacherForm
from .models import Teacher


class CreateTeacherView(CreateView):
    model = Teacher
    template_name = 'teachers/create.html'
    success_url = reverse_lazy('teachers:list')
    form_class = CreateTeacherForm


class DeleteTeacherView(DeleteView):
    model = Teacher
    template_name = 'teachers/delete.html'
    success_url = reverse_lazy('teachers:list')


class DetailTeacherView(DetailView):
    model = Teacher
    template_name = 'teachers/detail.html'


class ListTeacherView(ListView):
    model = Teacher
    template_name = 'teachers/list.html'


class UpdateTeacherView(UpdateView):
    model = Teacher
    template_name = 'teachers/update.html'
    success_url = reverse_lazy('teachers:list')
    form_class = EditTeacherForm


# def get_teachers(request):
#     teachers = Teacher.objects.all()
#     filter_form = TeacherFilterForm(request.GET, queryset=teachers)
#     return render(request, 'teachers/list.html', {'filter_form': filter_form})


# def create_teacher(request):
#     form = CreateTeacherForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return HttpResponseRedirect(reverse('teachers:list'))
#     return render(request, 'teachers/create.html', {'form': form})


# def detail_teacher(request, teacher_id):
#     teacher = get_object_or_404(Teacher, pk=teacher_id)
#     return render(request, 'teachers/detail.html', {'teacher': teacher})


# def update_teacher(request, teacher_id):
#     instance = get_object_or_404(Teacher, pk=teacher_id)
#     form = EditTeacherForm(request.POST or None, instance=instance)
#     if form.is_valid():
#         form.save()
#         return HttpResponseRedirect(reverse('teachers:list'))

#     return render(request, 'teachers/update.html', {'form': form})


# def delete_teacher(request, teacher_id):
#     teacher = get_object_or_404(Teacher, pk=teacher_id)
#     if request.method == 'POST':
#         teacher.delete()
#         return HttpResponseRedirect(reverse('teachers:list'))
#     return render(request, 'teachers/delete.html', {'teacher': teacher})
