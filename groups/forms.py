from django import forms

from django_filters import FilterSet

from .models import Group


class GroupBaseForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'

        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }


class GroupCreateForm(GroupBaseForm):
    from students.models import Student
    students = forms.ModelMultipleChoiceField(queryset=Student.objects.select_related('group'), required=False)

    def save(self, commit=True):
        group = super().save(commit)
        students = self.cleaned_data['students']
        for student in students:
            student.group = group
            student.save()

    class Meta(GroupBaseForm.Meta):
        pass


class GroupUpdateForm(GroupBaseForm):
    class Meta(GroupBaseForm.Meta):
        exclude = [
            'start_date',
        ]


class GroupFilterForm(FilterSet):
    class Meta:
        model = Group
        fields = {
            'name': ['icontains'],
            'course': ['exact'],
        }
