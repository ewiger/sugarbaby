from django import template
import sugarbaby


register = template.Library()


@register.simple_tag
def sugarbaby_version():
    return sugarbaby.__version__
