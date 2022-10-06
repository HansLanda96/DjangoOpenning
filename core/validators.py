from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

# Functional validator for Students model email field
# def validate_email_domains(value):
#     valid_domains = ['@gmail.com', '@yahoo.com']
#     for domain in valid_domains:
#         if domain in value:
#             break
#     else:
#         raise ValidationError('Invalid email domain')


# disable this validator for now
# def unique_email_validator(value):
#     from .models import Student
#     if Student.objects.filter(email=value).exists():
#         raise ValidationError(f'Student with email {value} already exists. Try to Log In.')


@deconstructible
class ValidEmailDomain:
    def __init__(self, *domains):
        self.domains = list(domains)

    def __call__(self, *args, **kwargs):
        for domain in self.domains:
            if args[0].endswith(domain):
                break

        else:
            raise ValidationError(f'Invalid email domain. The domain <{args[0].split("@")}> is not valid')
