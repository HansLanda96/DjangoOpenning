from datetime import date

from django.core.validators import MinLengthValidator
from django.db import models

from faker import Faker

from .validators import ValidEmailDomain

VALID_DOMAIN_LIST = ('@gmail.com', '@yahoo.com', '@test.com')


class Student(models.Model):
    first_name = models.CharField(
        max_length=100,
        verbose_name='First Name',
        db_column='first_name_column',
        validators=[MinLengthValidator(2, 'First name must be at least 2 characters long')]
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name='Last Name',
        db_column='last_name',
        validators=[MinLengthValidator(2, 'Last name must be at least 2 characters long')],
        error_messages={'min_length': 'Last name must be at least 2 characters long'}
    )
    birthday = models.DateField(default=date.today, null=True, blank=True)

    email = models.EmailField(validators=[ValidEmailDomain(*VALID_DOMAIN_LIST)])

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        db_table = 'student_table'

    @classmethod
    def generate_fake_data(cls, cnt):
        f = Faker()

        for _ in range(cnt):
            first_name = f.first_name()
            last_name = f.last_name()
            email = f'{first_name}.{last_name}{f.random.choice(VALID_DOMAIN_LIST)}'
            birthday = f.date()
            st = cls(first_name=first_name, last_name=last_name, email=email, birthday=birthday)
            try:
                st.full_clean()
                st.save()
            except:
                print(f'Error while saving {st}')
