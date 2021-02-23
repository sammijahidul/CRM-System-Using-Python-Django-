from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import *
from .forms import OrderForm, CreateUserForm
from .filters import orderFilter
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'accounts/register.html', context)

def loginPage(request):
    context = {}

    return render(request, 'accounts/login.html', context)

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
    myFilter = orderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context = {'customer':customer,'orders': orders,'order_count':order_count, 'myFilter': myFilter}
    return render(request,'accounts/customer.html',context)

def createOrder(request, new_value):
    OrderForSet = inlineformset_factory(Customer, Order, fields=('product','status'), extra=10 )
    customer = Customer.objects.get(id=new_value)
    formset = OrderForSet(queryset=Order.objects.none(),instance=customer)
    #form = OrderForm(initial={'customer': customer})
    if request.method == 'POST':
        formset = OrderForSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')


    context = {'formset': formset}

    return render(request, 'accounts/order_form.html', context)

def updateOrder(request, new_value):
    order = Order.objects.get(id=new_value)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context ={'form':form,}
    return render(request, 'accounts/order_form.html', context)

def deleteOrder(request, new_value):
    order = Order.objects.get(id=new_value)
    context = {'item':order}
    if request.method == 'POST':
        order.delete()
        return redirect('/')

    return render(request, 'accounts/delete.html',context)
