from django.contrib import admin

from groups.models import Group

from .models import Student


class GroupListFilter(admin.SimpleListFilter):
    title = 'group filter'
    parameter_name = 'group_filter'

    def lookups(self, request, model_admin):
        groups = Group.objects.all().order_by('name')
        lst = [(group.pk, group.name) for group in groups]
        lst.insert(0, (0, 'No group'))
        return tuple(lst)

    def queryset(self, request, queryset):
        match self.value():
            case None:
                return Student.objects.all()
            case '0':
                return Student.objects.filter(group__isnull=True)
            case _:
                return Student.objects.filter(group=Group.objects.get(pk=int(self.value())))


class StudentAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'group_name')
    list_display_links = list_display
    list_per_page = 15
    list_filter = (GroupListFilter, )

    fieldsets = (
        ('Personal info', {'fields': ('last_name', 'first_name')}),
        ('Birthday', {'fields': ('birthday', 'age')}),
        (None, {'fields': ('email', 'phone_number')}),
        (None, {'fields': ('group',)}),
    )

    def group_name(self, instance):
        if instance.group:
            return instance.group.name
        return ''

    group_name.short_description = 'group'

    def age(self, instance):
        if instance.get_age():
            return f'{instance.get_age()} y.o.'
        return 'Age is not specified'
    readonly_fields = ('age',)
    age.short_description = 'age'


admin.site.register(Student, StudentAdmin)
