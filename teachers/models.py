from datetime import date

from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

from students.models import VALID_DOMAIN_LIST
from students.validators import ValidEmailDomain


class Teacher(models.Model):
    FIELD_OF_STUDY_CHOICES = [
        ('Programming', (
            ('front-end', 'Front-End'),
            ('java', 'Java'),
            ('php', 'PHP'),
            ('python', 'Python'),
            ('devops', 'Devops'),
            ('machine-learning', 'Machine Learning'),
            ('c-sharp', 'C#'),
        )),
        ('Quality Assurance', (
            ('qa-manual', 'QA Manual'),
            ('qa-automation-java', 'QA Automation Java'),
            ('qa-automation-java', 'QA Automation Python'),
        )),
        ('Management', (
            ('project-management', 'Project Management'),
            ('product-management', 'Product Management'),
            ('hr', 'Recruitment & HR'),
            ('business-analyst', 'Business Analyst'),
        )),
        ('Marketing', (
            ('internet-marketing', 'Internet Marketing'),
            ('smm', 'Social Media Marketing'),
            ('smm-pro', 'SMM Pro'),
            ('inter-mark-for-business', 'Internet Marketing for Business'),
        )),
        ('Design', (
            ('ux-ui', 'UX/UI Design'),
        )),
        ('Children Education', (
            ('front-end-kids', 'Front-end(Kids)'),
            ('python-kids', 'Python(Kids)'),
            ('design-kids', 'Design(Kids)'),
            ('java-kids', 'Java(Kids)'),
        )),
    ]

    first_name = models.CharField(
        max_length=100,
        verbose_name='First Name',
        db_column='first_name',
        validators=[MinLengthValidator(2, 'First name must be at least 2 characters long')]
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name='Last Name',
        db_column='last_name',
        validators=[MinLengthValidator(2, 'Last name must be at least 2 characters long')],
    )
    birthday = models.DateField(default=date.today, null=True, blank=True)
    email = models.EmailField(validators=[ValidEmailDomain(*VALID_DOMAIN_LIST)], unique=True)
    phone_number = models.CharField(
        max_length=20,
        verbose_name='Phone Number',
        db_column='phone_number',
        blank=True,
    )
    specialization = models.CharField(
        db_column='specialization',
        max_length=25,
        choices=FIELD_OF_STUDY_CHOICES,
    )

    class Meta:
        db_table = 'teachers_table'

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.specialization}'

    @classmethod
    def generate_fake_teachers(cls, cnt):
        from faker import Faker
        f = Faker()
        for _ in range(cnt):
            first_name = f.first_name()
            last_name = f.last_name()
            email = f'{first_name}.{last_name}{f.random.choice(VALID_DOMAIN_LIST)}'
            birthday = f.date_between(start_date='-50y', end_date='-20y')
            specialization = f.random.choice(
                [specialization for _, specializations in cls.FIELD_OF_STUDY_CHOICES
                 for specialization in specializations]
            )[0].lowercase()
            teacher = cls(first_name=first_name, last_name=last_name, email=email,
                          birthday=birthday, specialization=specialization)
            try:
                teacher.full_clean()
                teacher.save()
            except ValidationError:
                print(f'Error while saving {teacher}')
