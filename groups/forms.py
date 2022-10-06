from django import forms

from .models import Group


class CreateGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'
        widgets = {'start_date': forms.DateInput(attrs={'type': 'date'})}


class UpdateGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'
        widgets = {'start_date': forms.DateInput(attrs={'type': 'date'})}
