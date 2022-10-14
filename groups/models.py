import datetime

from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateField(default=datetime.datetime.utcnow)
    end_date = models.DateField(null=True, blank=True)
    headman = models.OneToOneField(
        'students.Student',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='headman_group'
    )
    create_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)
    course = models.OneToOneField(  # add course model to the group
        'courses.Course',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='course_group'
    )

    class Meta:
        db_table = 'lms_groups_table'

    def __str__(self):
        return f'Group name: <{self.name}>'
