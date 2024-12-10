from django import template

register = template.Library()


@register.filter
def get_dict_value(dictionary, key):
    """Get the value from a dictionary, or return None if the key doesn't exist."""
    return dictionary.get(key, 0)  # Default to 0 if the key doesn't exist