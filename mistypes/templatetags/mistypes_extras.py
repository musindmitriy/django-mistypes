
from django import template

register = template.Library()


@register.inclusion_tag('mistypes/mistype-form.html')
def mistype_form():
    return {}

