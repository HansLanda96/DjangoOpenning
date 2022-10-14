from django.db import models


class Course(models.Model):
    CATEGORIES = [
        ('Software Development', 'Software Development'),
        ('Quality Assurance', 'Quality Assurance'),
        ('Management', 'Management'),
        ('Marketing', 'Marketing'),
        ('Web Design', 'Web Design'),
        ('Kids', 'Kids'),
    ]
    course = models.CharField(
        max_length=100,
        db_column='course',
        verbose_name='Course',
    )
    subject = models.CharField(
        max_length=100,
        db_column='subject',
        verbose_name='Subject',
        blank=True
    )
    category = models.CharField(
        max_length=100,
        db_column='category',
        verbose_name='Category',
        choices=CATEGORIES,
    )
    price = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        db_column='price(UAH)',
        verbose_name='Price',
    )
    amount_lessons = models.IntegerField(
        db_column='amount_of_lessons',
        verbose_name='Lessons',
        default=16,
    )
    technologies = models.TextField(
        db_column='technologies',
        verbose_name='Technologies',
    )

    def __str__(self):
        return f"{self.course} - {self.category}"

    class Meta:
        db_table = 'lms_courses_table'
