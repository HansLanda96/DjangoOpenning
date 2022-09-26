import re

from django import forms

from .models import Student


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

    def clean(self):
        pass

    def clean_birthday(self):
        return self.cleaned_data.get('birthday')

    def clean_first_name(self):
        return self.cleaned_data.get('first_name').lower().capitalize()

    def clean_last_name(self):
        return self.cleaned_data.get('last_name').lower().capitalize()

    def clean_phone_number(self):
        phone_without_symbols = re.sub(r'\D', '', self.cleaned_data.get('phone_number'))
        if 13 > len(phone_without_symbols) >= 10:
            format_phone = re.sub(
                r"^(.*?)(0)(39|50|66|95|99|67|68|89|91|92|94|96|97|98|[679]3)(\d{3})(\d{2})(\d{2})$",
                r"+38\2(\3)-\4-\5-\6",
                phone_without_symbols
            )
            if format_phone == phone_without_symbols:
                raise forms.ValidationError(
                    'Phone number is not match any Ukrainian cellular operator'
                )
            else:
                return format_phone
        else:
            if len(phone_without_symbols) >= 13:
                raise forms.ValidationError('Phone number is too long >= 13 digits')
            else:
                raise forms.ValidationError('Phone number is too short (Less than 10 digits)')


class EditStudentForm(CreateStudentForm):
    class Meta(CreateStudentForm.Meta):
        exclude = ['birthday']
