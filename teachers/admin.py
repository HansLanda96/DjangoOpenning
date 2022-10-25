from django.contrib import admin


from .models import Teacher


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'specialization', 'format_salary')
    list_display_links = list_display
    list_per_page = 15
    list_filter = ['specialization']
    ordering = ['last_name']

    fieldsets = (
        ('Personal info', {'fields': ('last_name', 'first_name')}),
        ('Birthday', {'fields': ('birthday', 'age')}),
        ('Contacts', {'fields': ('email', 'phone_number')}),
        ('Additional info', {'fields': ('specialization', 'salary')}),
    )

    def age(self, instance):
        if instance.get_age():
            return f'{instance.get_age()} y.o.'
        return 'Age is not specified'
    readonly_fields = ('age',)
    age.short_description = 'age'

    def format_salary(self, instance):
        return "{:,} $".format(instance.salary)
    format_salary.short_description = 'salary'


admin.site.register(Teacher, TeacherAdmin)
