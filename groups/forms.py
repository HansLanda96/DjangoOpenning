from django import forms

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
    def __init__(self, *args, **kwargs):
        from students.views import Student
        super().__init__(*args, **kwargs)
        self.fields['students'] = forms.ModelMultipleChoiceField(
            queryset=Student.objects.select_related('group'),
            required=False,
        )

    class Meta(GroupBaseForm.Meta):
        exclude = [
            'headman',
        ]


class GroupUpdateForm(GroupBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['headman_field'] = forms.ChoiceField(
            choices=[
                (student.pk, f'{student.first_name} {student.last_name}') for student in self.instance.students.all()
            ],
            label='Headman',
            required=False,
        )
        self.fields['headman_field'].choices.insert(0, (0, '---------'))

    class Meta(GroupBaseForm.Meta):
        exclude = [
            'start_date',
            'headman',
        ]
