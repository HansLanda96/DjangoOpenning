from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView


from .forms import CourseCreateForm, CourseUpdateForm
from .models import Course


class CreateCourseView(CreateView):
    model = Course
    template_name = 'courses/create.html'
    success_url = reverse_lazy('courses:list')
    form_class = CourseCreateForm


class DeleteCourseView(DeleteView):
    model = Course
    template_name = 'courses/delete.html'
    success_url = reverse_lazy('courses:list')


class DetailCourseView(DetailView):
    model = Course
    template_name = 'courses/detail.html'


class ListCourseView(ListView):
    model = Course
    template_name = 'courses/list.html'


class UpdateCourseView(UpdateView):
    model = Course
    template_name = 'courses/update.html'
    success_url = reverse_lazy('courses:list')
    form_class = CourseUpdateForm


# def create_course(request):
#     form = CourseCreateForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return HttpResponseRedirect(reverse('courses:list'))
#     return render(request, 'courses/create.html', {'form': form})


# def delete_course(request, course_id):
#     course = get_object_or_404(Course, pk=course_id)
#     if request.method == 'POST':
#         course.delete()
#         return HttpResponseRedirect(reverse('course:list'))
#     return render(request, 'courses/delete.html', {'course': course})


# def detail_course(request, course_id):
#     course = get_object_or_404(Course, pk=course_id)
#     return render(request, 'courses/detail.html', {'course': course})


# def get_course(request):
#     courses = Course.objects.all()
#     filter_form = CourseFilterForm(request.GET, queryset=courses)
#     return render(request, 'courses/list.html', {'courses': courses, 'filter_form': filter_form})


# def update_course(request, course_id):
#     course = get_object_or_404(Course, pk=course_id)
#     if request.method == 'POST':
#         form = CourseUpdateForm(instance=course, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('courses:list'))
#     form = CourseUpdateForm(instance=course)
#     return render(request, 'courses/update.html', {'form': form, 'course': course})
