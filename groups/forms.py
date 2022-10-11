from django import forms

from django_filters import FilterSet

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


class GroupFilterForm(FilterSet):
    class Meta:
        model = Group
        fields = {
            'name': ['exact', 'icontains'],
            'start_date': ['exact', 'startswith'],
        }
