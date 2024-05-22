from django.shortcuts import render,redirect
from django.template import loader
from .models import Cart
from products.models import Product
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def add_to_cart(request,pid):
    id=pid
    quantity=1
    prod=Product.objects.get(pid=id)
    Cart.objects.create(product=prod,quantity=1,pid=prod.pid,price=prod.price)
    print(id)
    return redirect('products:details')

def remove_from_cart(request,pid):
    id=pid
    prod=Product.objects.get(pid=id)
    Cart.objects.filter(product=prod).delete()
    return redirect('cart:show_cart')

def show_cart(request):
    data = Cart.objects.all().values()
    dat = Cart.objects.values('product')
    to_find=[i['product'] for i in dat]
    new_data = Product.objects.filter(pid__in=to_find).values()
    context = {
        'cart': data,
        'quantity': new_data,
    }
    return render(request, 'cart.html', context)

@require_POST
def update_cart(request, product_id):
    new_quantity = request.POST.get('new_quantity')
    cart_item = Cart.objects.get(pid=product_id)
    cart_item.quantity = new_quantity
    cart_item.save()
    return redirect('cart:show_cart')

def clear_cart(request):
    Cart.objects.all().delete()
    messages.success(request, 'Cart cleared successfully')
    return redirect('cart:show_cart')
