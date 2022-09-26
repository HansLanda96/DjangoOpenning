from datetime import date

from django.core.exceptions import ValidationError


def validate_start_date(value):
    if value < date.today():
        raise ValidationError(f'Start date must be greater or equal today\'s date <{date.today()}>')
