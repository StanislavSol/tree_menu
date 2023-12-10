from django.urls import path
from menu_app import views

urlpatterns = [
        path('<str:menu_name>/', views.draw_menu, name='draw_menu'),
]
