from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView


from .forms import CreateStudentForm, UpdateStudentForm
from .models import Student


class CreateStudentView(CreateView):
    model = Student
    template_name = 'students/create.html'
    success_url = reverse_lazy('students:list')
    form_class = CreateStudentForm


class DeleteStudentView(DeleteView):
    model = Student
    template_name = 'students/delete.html'
    success_url = reverse_lazy('students:list')


class DetailStudentView(DetailView):
    model = Student
    template_name = 'students/detail.html'


class ListStudentView(ListView):
    model = Student
    template_name = 'students/list.html'


class UpdateStudentView(UpdateView):
    model = Student
    template_name = 'students/update.html'
    success_url = reverse_lazy('students:list')
    form_class = UpdateStudentForm


# def get_students(request):
#     students = Student.objects.select_related('group')

#     filter_form = StudentFilterForm(data=request.GET, queryset=students)

#     return render(
#         request=request,
#         template_name='students/list.html',
#         context={'filter_form': filter_form}
#     )


# def detail_student(request, student_id):
#     student = Student.objects.get(pk=student_id)
#     return render(request, 'students/detail.html', {'student': student})


# def create_student(request):
#     if request.method == 'GET':
#         form = CreateStudentForm()
#     elif request.method == 'POST':
#         form = CreateStudentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('students:list'))
#     return render(request, 'students/create.html', {'form': form})


# class UpdateStudentView(UpdateView):
#     model = Student
#     form_class = UpdateStudentForm
#     success_url = reverse_lazy('students:list')
#     template_name = 'students/update.html'


# def delete_student(request, student_id):
#     student = get_object_or_404(Student, pk=student_id)        # Http404
#     if request.method == 'POST':
#         student.delete()
#         return HttpResponseRedirect(reverse('students:list'))
#     return render(request, 'students/delete.html', {'student': student})
