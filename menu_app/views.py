from django.shortcuts import render
from .models import Menu


def draw_menu(request, menu_name):
    menu_items = Menu.objects.filter(name=menu_name).select_related('parent')
    return render(request, 'menu.html', {'menu_items': menu_items})
