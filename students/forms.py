from django import forms

from .models import Student
from .utils import validate_phone_number


class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [      # __all__ for all fields
            'first_name',
            'last_name',
            'birthday',
            'email',
            'phone_number',
        ]

        widgets = {'birthday': forms.DateInput(attrs={'type': 'date'})}

    def clean(self):
        pass

    def clean_birthday(self):
        return self.cleaned_data.get('birthday')

    def clean_first_name(self):
        return self.cleaned_data.get('first_name').lower().capitalize()

    def clean_last_name(self):
        return self.cleaned_data.get('last_name').lower().capitalize()

    def clean_phone_number(self):
        return validate_phone_number(self.cleaned_data.get('phone_number'))


class EditStudentForm(CreateStudentForm):
    class Meta(CreateStudentForm.Meta):
        exclude = ['birthday']
