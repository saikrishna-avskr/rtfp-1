from django.shortcuts import render,redirect
from .models import Cart
from products.models import Product
from django.views.decorators.http import require_POST
from django.contrib import messages

def add_to_cart(request,pid):
    id=pid
    quantity=1
    prod=Product.objects.get(pid=id)
    Cart.objects.create(product=prod,quantity=1,pid=prod.pid,price=prod.price)
    return redirect('products:details')

def remove_from_cart(request,pid):
    id=pid
    prod=Product.objects.get(pid=id)
    Cart.objects.filter(product=prod).delete()
    messages.success(request, 'Product removed from cart successfully')
    return redirect('cart:show_cart')

def show_cart(request):
    data = Cart.objects.all().values()
    dat = Cart.objects.values('product')
    update_tot_price()
    to_find=[i['product'] for i in dat]
    new_data = Product.objects.filter(pid__in=to_find).values()
    first_cart_item = Cart.objects.first()
    if first_cart_item is not None:
        tot_price = round(first_cart_item.tot_price,2)
    else:
        tot_price="No items in Cart"
    context = {
        'cart': data,
        'quantity': new_data,
        'tot_price': tot_price,
    }
    print(context)
    return render(request, 'cart.html', context)

@require_POST
def update_cart(request, product_id):
    new_quantity = request.POST.get('new_quantity')
    price = Product.objects.get(pid=product_id).price
    print(price)
    new_price = int(new_quantity) * price
    cart_item = Cart.objects.get(pid=product_id)
    cart_item.quantity = new_quantity
    cart_item.price = new_price
    cart_item.save()
    return redirect('cart:show_cart')

def clear_cart(request):
    Cart.objects.all().delete()
    messages.success(request, 'Cart cleared successfully')
    return redirect('cart:show_cart')

def update_tot_price():
    total = 0
    for i in Cart.objects.all():
        total += i.price
    Cart.objects.all().update(tot_price=total)
    
def check_out(request):
    return render(request, 'patient.html')


def order(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        
        data = Cart.objects.all().values()
        dat = Cart.objects.values('product')
        to_find=[i['product'] for i in dat]
        new_data = Product.objects.filter(pid__in=to_find).values()
        first_cart_item = Cart.objects.first()        
        if first_cart_item is not None:
            tot_price = first_cart_item.tot_price
            print(tot_price)
        else:
            tot_price="No items in Cart"
        
        cart_items = Cart.objects.all()
        product_ids = [item.product.pid for item in cart_items]
        products = Product.objects.filter(pid__in=product_ids)

        context = {
            'cart': data,
            'quantity': new_data,
            'tot_price': tot_price,
            'name':name,
            'gender':gender,
            'dob':dob,
            'age':age,
            'phone':phone,
        }
        print(context)
        for product in products:
            cart_item = cart_items.get(product__pid=product.pid)
            product.stock -= cart_item.quantity 
            product.save()
        return render(request, 'invoice.html', context)
        
    return render(request,'patient.html')

def del_cart(request):
    Cart.objects.all().delete()
    return redirect('products:details')