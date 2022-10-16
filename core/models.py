from datetime import date

from core.validators import ValidEmailDomain

from dateutil.relativedelta import relativedelta

from django.core.validators import MinLengthValidator
from django.db import models

from faker import Faker


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class PersonaModel(BaseModel):
    VALID_DOMAIN_LIST = ('@gmail.com', '@yahoo.com', '@test.com')
    first_name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2, '"First name" field value less than two symbols')]
    )
    last_name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2, '"Last name" field value less than two symbols')],
    )
    birthday = models.DateField(default=date.today, null=True, blank=True)
    email = models.EmailField(validators=[ValidEmailDomain(*VALID_DOMAIN_LIST)])
    phone_number = models.CharField(
        max_length=20,
        verbose_name='Phone Number',
        db_column='telephone',
        blank=True,
    )

    class Meta:
        abstract = True

    def get_age(self):
        return relativedelta(date.today(), self.birthday).years

    @classmethod
    def _generate(cls):
        f = Faker('it_IT')
        first_name = f.first_name()
        last_name = f.last_name()
        obj = cls(
            first_name=first_name,
            last_name=last_name,
            birthday=f.date_between(start_date='-65y', end_date='-13y'),
            email=f'{first_name}.{last_name}{f.random.choice(cls.VALID_DOMAIN_LIST)}',
        )

        obj.save()
        return obj

    @classmethod
    def generator(cls, cnt):
        for _ in range(cnt):
            cls._generate()
