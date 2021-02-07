from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customer = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders':orders, 'customers':customers,
    'total_orders': total_orders, 'delivered': delivered,
    'pending': pending}

    return render(request,'accounts/dashboard.html', context)

def products(request):
    products = Products.objects.all()
    return render(request,'accounts/products.html', {'product': products})

def customer(request, new_value):
    customer = Customer.objects.get(id=new_value)
    orders = customer.order_set.all()
    order_count = orders.count()

    context = {'customer':customer,'orders': orders,'order_count':order_count}
    return render(request,'accounts/customer.html',context)
