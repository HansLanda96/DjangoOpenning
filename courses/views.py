from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .forms import CourseCreateForm, CourseFilterForm, CourseUpdateForm
from .models import Course


def create_course(request):
    form = CourseCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('courses:list'))
    return render(request, 'courses/create.html', {'form': form})


def delete_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        course.delete()
        return HttpResponseRedirect(reverse('course:list'))
    return render(request, 'courses/delete.html', {'course': course})


def detail_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'courses/detail.html', {'course': course})


def get_course(request):
    courses = Course.objects.all()
    filter_form = CourseFilterForm(request.GET, queryset=courses)
    return render(request, 'courses/list.html', {'courses': courses, 'filter_form': filter_form})


def update_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form = CourseUpdateForm(instance=course, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('courses:list'))
    form = CourseUpdateForm(instance=course)
    return render(request, 'courses/update.html', {'form': form, 'course': course})
