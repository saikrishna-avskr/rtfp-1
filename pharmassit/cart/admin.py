from django.contrib import admin
from .models import Cart

class CartAdmin(admin.ModelAdmin):
    list_display = ('product','quantity','price')
    
admin.site.register(Cart,CartAdmin)