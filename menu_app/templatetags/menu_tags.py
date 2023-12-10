from django import template
from menu_app.models import Menu
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def draw_menu(menu_name):
    menu_items = Menu.objects.filter(name=menu_name).select_related('parent')
    return mark_safe(sample_menu(menu_items))


def sample_menu(menu_element):
    result = '<ul>'
    for elem in menu_element:
        result += '<li>'
        if elem.url:
            result += f'<a href="{ elem.url }">{ elem.name }</a>'
        else:
            result += elem.name
        if elem.child.exists():
            result += sample_menu(elem.child.all())

        result += '</li>'
    result += '</ul>'
    return result
