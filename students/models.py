from datetime import date

from dateutil.relativedelta import relativedelta
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

from core.validators import ValidEmailDomain
from groups.models import Group

VALID_DOMAIN_LIST = ('@gmail.com', '@yahoo.com', '@test.com')


class Student(models.Model):
    first_name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2, f'"First name" field value less than two symbols')]
    )
    last_name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2)],
        error_messages={'min_length': '"last_name" field value less than two symbols'}
    )
    birthday = models.DateField(default=date.today, null=True, blank=True)
    email = models.EmailField(validators=[ValidEmailDomain(*VALID_DOMAIN_LIST)])
    phone_number = models.CharField(
        max_length=20,
        verbose_name='Phone Number',
        db_column='phone_number',
        blank=True,
    )
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, related_name='students', blank=True)
    create_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.group is None:
            return f'{self.first_name} {self.last_name}'
        else:
            return f'{self.first_name} {self.last_name} ({self.group.name})'

    def get_age(self):
        return relativedelta(date.today(), self.birthday).years

    class Meta:
        db_table = 'lms_students_table'

    @classmethod
    def generate_fake_data(cls, cnt):
        from faker import Faker
        f = Faker()
        for _ in range(cnt):
            first_name = f.first_name()
            last_name = f.last_name()
            email = f'{first_name}.{last_name}{f.random.choice(VALID_DOMAIN_LIST)}'
            birthday = f.date_between(start_date='-70y', end_date='-10y')
            st = cls(first_name=first_name, last_name=last_name, email=email, birthday=birthday)
            try:
                st.full_clean()
                st.save()
            except ValidationError as e:
                print(f'Error while saving {e}')
