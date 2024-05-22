from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('add/<int:pid>/', views.add_to_cart,name='add_to_cart'),
    path('remove/<int:pid>/', views.remove_from_cart,name='remove_from_cart'),
    path('show/', views.show_cart,name='show_cart'),
]