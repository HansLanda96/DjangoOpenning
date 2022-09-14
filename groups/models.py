from datetime import date

from django.core.validators import MinLengthValidator
from django.db import models


class Group(models.Model):
    name = models.CharField(
        max_length=100,
        help_text='Create name for group. Example: "Python-12" or "PythonPro-Hillel-Kiseev"',
        verbose_name='Group Name',
        db_column='group_name',
        validators=[MinLengthValidator(10, 'Group name must be at least 10 characters long')],
        unique=True
    )
    start_date = models.DateField(
        default=date.today,
        max_length=10,
        verbose_name='Group Start Date',
        db_column='start_date'
    )
    description = models.TextField(
        default='Group Description',
        help_text='Enter a group description here.',
        verbose_name='Group Description',
        db_column='description'
    )
