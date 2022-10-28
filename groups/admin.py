from django.contrib import admin


from .models import Group


class StudetnInlineTable(admin.TabularInline):
    from students.models import Student
    model = Student
    fields = ('first_name', 'last_name')
    extra = 0
    readonly_fields = fields
    show_change_link = True

    def has_delete_permission(self, request, obj=None) -> bool:
        return False

    def has_add_permission(self, request, obj=None) -> bool:
        return False


class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'headman_info', 'course_fix', 'start_date', 'end_date', 'students_count')
    list_display_links = list_display
    list_per_page = 15
    list_filter = ['course', 'start_date']
    empty_value_display = '-not stated-'

    fieldsets = (
        (None, {'fields': ('name', 'course', 'headman')}),
    )

    def headman_info(self, instance):
        if instance.headman:
            return f'{instance.headman.last_name} {instance.headman.first_name}'
        return self.empty_value_display
    headman_info.short_description = 'headman'

    def students_count(self, instance):
        return instance.students.count()
    students_count.short_description = 'students count'

    def course_fix(self, instance):
        if instance.course:
            return instance.course.title()
        return self.empty_value_display
    course_fix.short_description = 'course'

    def formfield_for_foreignkey(self, db_field, request, **kwargs):    # choice headman from students in group
        if db_field.name == 'headman':
            kwargs['queryset'] = Group.objects.get(pk=request.resolver_match.kwargs['object_id']).students.all()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        form.base_fields['headman'].widget.can_add_related = False
        form.base_fields['headman'].widget.can_change_related = False
        form.base_fields['headman'].widget.can_delete_related = False
        return form

    inlines = [StudetnInlineTable, ]


admin.site.register(Group, GroupAdmin)
