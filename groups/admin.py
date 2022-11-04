from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from .models import Group


class StudetnInlineTable(admin.TabularInline):
    from students.models import Student
    model = Student
    fields = ('first_name', 'last_name', 'email')
    extra = 0
    readonly_fields = ('first_name', 'last_name')
    show_change_link = True

    def get_queryset(self, request):
        queryset = self.model.objects.filter(
            group_id=int(request.resolver_match.kwargs['object_id'])
        ).select_related('group')
        return queryset

    def has_delete_permission(self, request, obj=None) -> bool:
        return False

    def has_add_permission(self, request, obj=None) -> bool:
        return False

    def has_change_permission(self, request, obj=None) -> bool:
        return False


class TeacherInlineTable(admin.TabularInline):
    model = Group.teachers.through
    extra = 0
    fields = ['teacher_name', 'teacher_surname', 'teacher_email', 'teacher_spec']
    readonly_fields = fields

    def teacher_name(self, obj):
        return obj.teacher.first_name
    teacher_name.short_description = 'Teacher`s name'

    def teacher_surname(self, obj):
        return obj.teacher.last_name
    teacher_surname.short_description = 'Teacher`s surname'

    def teacher_email(self, obj):
        return obj.teacher.email
    teacher_email.short_description = 'Teacher`s email'

    def teacher_spec(self, obj):
        return obj.teacher.specialization.title()
    teacher_spec.short_description = 'Teacher`s specialization'

    def has_delete_permission(self, request, obj=None) -> bool:
        return False

    def has_add_permission(self, request, obj=None) -> bool:
        return False


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'headman_info', 'course_fix', 'start_date', 'end_date', 'students_count')
    list_per_page = 15
    list_filter = ['course', 'start_date']
    empty_value_display = '-not stated-'

    fields = (
        'name',
        'start_date',
        'end_date',
        'headman',
        ('created_at', 'updated_at'),
    )

    readonly_fields = ('created_at', 'updated_at')

    def headman_info(self, instance):
        if instance.headman:
            return f'{instance.headman.last_name} {instance.headman.first_name}'
        return self.empty_value_display
    headman_info.short_description = 'headman'

    def students_count(self, instance):
        count = instance.students.count()
        url = (
            reverse("admin:students_student_changelist") + '?' + urlencode({'group_id': f'{instance.pk}'})
        )
        return format_html('<a href="{}">{} student(s)</a>', url, count)
    students_count.short_description = 'Students'

    def course_fix(self, instance):
        if instance.course:
            return instance.course.title()
        return self.empty_value_display
    course_fix.short_description = 'course'

    # def formfield_for_foreignkey(self, db_field, request, **kwargs):  # choice headman from students in group
    #     if db_field.name == 'headman':
    #         kwargs['queryset'] = Group.objects.get(pk=request.resolver_match.kwargs['object_id']).students.all()
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        form.base_fields['headman'].widget.can_add_related = False
        form.base_fields['headman'].widget.can_change_related = False
        form.base_fields['headman'].widget.can_delete_related = False
        form.base_fields['headman'].queryset = obj.students.all()   # same as def formfield_for_foreignkey
        return form

    inlines = [StudetnInlineTable, TeacherInlineTable, ]
    # exclude = ['teachers', ]
