from django import forms

from django_filters import FilterSet

from students.utils import validate_phone_number

from .models import Teacher


class TeacherFilterForm(FilterSet):
    class Meta:
        model = Teacher
        fields = {
            'first_name': ['icontains'],
            'last_name': ['icontains'],
            'specialization': ['exact'],
        }


class CreateTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
            'specialization': forms.Select(attrs={'class': 'form-control'})
        }

    def clean_first_name(self):
        return self.cleaned_data.get('first_name').capitalize()

    def clean_last_name(self):
        return self.cleaned_data.get('last_name').capitalize()

    def clean_phone_number(self):
        return validate_phone_number(self.cleaned_data.get('phone_number'))


class EditTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            'first_name',
            'last_name',
            'phone_number',
            'specialization',
        ]
        widgets = {
            'specialization': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_first_name(self):
        return self.cleaned_data.get('first_name').capitalize()

    def clean_last_name(self):
        return self.cleaned_data.get('last_name').capitalize()

    def clean_phone_number(self):
        return validate_phone_number(self.cleaned_data.get('phone_number'))
