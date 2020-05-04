from django import template


register = template.Library()


@register.simple_tag
def bizz_or_fuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return 'BizzFuzz'
    elif number % 3 == 0:
        return 'Bizz'
    elif number % 5 == 0:
        return 'Fuzz'
    else:
        return number
