import re
from django.core.exceptions import ValidationError

def validate_password(value):
    if not re.search(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{6,}$', value):
        raise ValidationError(
            'Password must be at least 6 characters long and contain at least one letter, one number, and one symbol.'
        )
