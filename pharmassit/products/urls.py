from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('details/', views.details,name='details'),
    path('find_exp_items/', views.find_exp_items,name='find_exp_items'),
    path('find_low_stock/', views.low_stock,name='low_stock'),
    path('remove_product/<int:pid>/', views.remove_product,name='remove_product'),
]