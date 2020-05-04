from datetime import date
from django import template


register = template.Library()


@register.simple_tag
def is_eligible(birthday):
    today = date.today()
    age = today.year - birthday.year
    if today.month < birthday.month:
        age -= 1
    elif today.month == birthday.month and today.day < birthday.day:
        age -= 1
    if age > 13:
        return 'allowed'
    else:
        return 'blocked'
