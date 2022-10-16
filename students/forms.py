from django import forms

from django_filters import FilterSet

from .models import Student
from .utils import validate_phone_number


class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'birthday',
            'phone_number',
            'email',
        ]

        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }

    def clean_first_name(self):
        return self.cleaned_data.get('first_name').capitalize()

    def clean_last_name(self):
        return self.cleaned_data.get('last_name').capitalize()

    def clean_phone_number(self):
        return validate_phone_number(self.cleaned_data.get('phone_number'))


class UpdateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            # '__all__',
            'first_name',
            'last_name',
            'birthday',
            'phone_number',
        ]

        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }


class StudentFilterForm(FilterSet):
    class Meta:
        model = Student
        fields = {
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'startswith']
        }
