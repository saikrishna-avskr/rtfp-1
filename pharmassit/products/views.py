from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.template import loader
from django.db.models import Q
from .models import Product
from cart.models import Cart
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from datetime import datetime
from dateutil.relativedelta import relativedelta
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def index(request):
    return render(request,'index.html')

@login_required(login_url='/admin/login/',redirect_field_name='next',)
@csrf_exempt
def details(request):
    if request.method == 'POST':
        name = request.POST.get('sample')
        if name == '':
            name = 'No data'
        if name == 'all':
            mydata = Product.objects.all().values()
        else:  
            mydata = Product.objects.filter(Q(name__icontains=name) | Q(generic_name__icontains=name)).values()
        template = loader.get_template('details.html')
        dat = Cart.objects.values('product')
        to_find=[i['product'] for i in dat]
        data = Product.objects.filter(pid__in=to_find).values()        
        context = {
            'myproducts': mydata,
            'incart': data,
        }   
        return render(request,'details.html',context)
    else: 
        template = loader.get_template('details.html')
        return HttpResponse(template.render())

def find_exp_items(request):
    today = datetime.today()
    last_month = today + relativedelta(months=1)
    f_date=last_month.date()
    data = Product.objects.filter(expiry_date__lt=f_date).values()
    context = {
        'exp_products': data,
    }
    return render(request,'details.html',context)

def low_stock(request):
    data = Product.objects.filter(stock__lt=10).values()
    context = {
        'lowproducts': data,
    }
    return render(request,'details.html',context)

def remove_product(request,pid):
    id=pid
    prod=Product.objects.get(pid=id)
    prod.delete()
    return redirect('products:details')

def show_upload(request):
    return render(request,'selectFile.html')

def upload_report(request):
    if request.method == 'POST':
        handle_uploaded_file(request.FILES["myfile"])
        return render(request,'details.html')
    else:
        return render(request,'selectFile.html')

def handle_uploaded_file(f):
    with open(BASE_DIR/"name.png", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    text = pytesseract.image_to_string(Image.open(BASE_DIR/"name.png"))
    words = text.split(' ')
    
    for word in words:
        if len(word) == 8: 
            products = Product.objects.filter(Q(name__icontains=word) | Q(generic_name__icontains=word))
            print(products)
            for product in products:
                
                cart_item, created = Cart.objects.get_or_create(product_id=product.pid, defaults={'quantity': 1, 'price': product.price, 'tot_price': product.price})
                if not created:
                    # If the cart item already exists, increase the quantity
                    cart_item.quantity += 1
                    cart_item.tot_price += product.price
                    cart_item.save()
    print(text)