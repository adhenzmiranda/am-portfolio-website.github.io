from django import template
from ..models import TECH_STACK_CHOICES

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def tech_display(value):
    # Flatten grouped choices
    flat_choices = []
    for group in TECH_STACK_CHOICES:
        flat_choices.extend(group[1])
    return dict(flat_choices).get(value, value)