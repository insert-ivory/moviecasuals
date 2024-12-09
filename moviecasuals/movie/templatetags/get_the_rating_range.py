from django import template

register = template.Library()


@register.filter
def generate_range(value):
    try:
        return range(1, int(value) + 1)
    except (ValueError, TypeError):
        return []