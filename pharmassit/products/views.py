from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.template import loader
from .models import Product
from cart.models import Cart
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from datetime import datetime
from dateutil.relativedelta import relativedelta

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
            mydata = Product.objects.filter(name__icontains=name).values()
        template = loader.get_template('details.html')
        dat = Cart.objects.values('product')
        to_find=[i['product'] for i in dat]
        data = Product.objects.filter(pid__in=to_find).values()        
        #data=[i['product'] for i in dat]
        print(data)
        print("\n\n")
        print(mydata)
        
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
    last_month = today - relativedelta(months=1)
    f_date=last_month.date()
    formatted_date = f_date.strftime('%d-%m-%Y')
    #print(formatted_date)
    data = Product.objects.filter(expiry_date__lt=formatted_date).values()
    template = loader.get_template('details.html')
    context = {
        'exp_products': data,
    }
    return render(request,'details.html',context)

def low_stock(request):
    data = Product.objects.filter(stock__lt=10).values()
    template = loader.get_template('details.html')
    context = {
        'lowproducts': data,
    }
    return render(request,'details.html',context)
