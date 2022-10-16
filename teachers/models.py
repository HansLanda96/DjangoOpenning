from core.models import PersonaModel

from django.db import models


class Teacher(PersonaModel):
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
    salary = models.PositiveIntegerField(default=10_000)
    specialization = models.CharField(
        db_column='specialization',
        max_length=25,
        choices=FIELD_OF_STUDY_CHOICES,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.specialization} (${self.salary})'

    class Meta:
        db_table = 'lms_teachers'
