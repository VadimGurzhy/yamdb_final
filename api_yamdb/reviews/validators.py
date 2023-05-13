import datetime as dt

from django.core.exceptions import ValidationError


def validate_year(year):
    current_day = dt.date.today()
    if year > current_day.year:
        raise ValidationError(f'Некорректный год: {year}')
