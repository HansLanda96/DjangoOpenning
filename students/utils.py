import re

from django.core.exceptions import ValidationError


def validate_phone_number(value):
    phone_without_symbols = re.sub(r'\D', '', value)
    if 13 > len(phone_without_symbols) >= 10:
        format_phone = re.sub(
            r"^(.*?)(0)(39|50|66|95|99|67|68|89|91|92|94|96|97|98|[679]3)(\d{3})(\d{2})(\d{2})$",
            r"+38\2(\3)-\4-\5-\6",
            phone_without_symbols
        )
        if format_phone == phone_without_symbols:
            raise ValidationError(
                'Phone number is not match any Ukrainian cellular operator'
            )
        else:
            return format_phone
    else:
        if len(phone_without_symbols) >= 13:
            raise ValidationError('Phone number is too long >= 13 digits')
        else:
            raise ValidationError('Phone number is too short (Less than 10 digits)')
