from django import template

register = template.Library()

@register.filter(name='charcount')
def charcount(value):
    return len(value)

