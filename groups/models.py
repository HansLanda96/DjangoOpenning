import datetime

from faker import Faker

from core.models import BaseModel

from django.db import models


class Group(BaseModel):
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
    course = models.OneToOneField(
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

    @classmethod
    def gen_group(cls, cnt):
        f = Faker('it_IT')
        for _ in range(cnt):
            name = f.text(max_nb_chars=18)
            gr = cls(name=name)
            gr.save()
