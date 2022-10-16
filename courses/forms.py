from django import forms

from django_filters import FilterSet

from .models import Course


class CourseBaseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

        widgets = {
            'price': forms.NumberInput(attrs={'type': 'number'}),
            'amount_lessons': forms.NumberInput(attrs={'type': 'number'}),
        }

    def clean_course(self):
        return self.cleaned_data.get('course').title()

    def clean_subject(self):
        return self.cleaned_data.get('subject').title()

    def clean_category(self):
        return self.cleaned_data.get('category').title()


class CourseCreateForm(CourseBaseForm):
    class Meta:
        model = Course
        fields = '__all__'


class CourseUpdateForm(CourseBaseForm):
    class Meta(CourseBaseForm.Meta):
        exclude = [
            'category',
        ]


class CourseFilterForm(FilterSet):
    class Meta:
        model = Course
        fields = {
            'category': ['exact'],
        }
