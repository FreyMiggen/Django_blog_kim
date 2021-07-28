from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import SignUpForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import Group

from django.contrib import messages
from django.contrib.auth.decorators import login_required # add @login_required(login_urls='') for every view that you want only logged in account to see

from .decorators import unauthenticated_user,allowed_users
from .models import Customer,Tag,Product,Order
from .forms import *

@allowed_users(allowed_roles=['admin'])
def home_view(request):                                   # otherwise they will be redirected to ''
    return render(request,'bases.html',{})

# Create your views here.


@unauthenticated_user
def UserRegisterView(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)                
        if form.is_valid():
                        #form.save()
            user=form.save()
                            # to make every person register automatically enter group 'outsider'
            group=Group.objects.get(name='outsider')
            group.user_set.add(user)
            print(group.name)
            username=form.cleaned_data.get('username')
            messages.success(request,'User '+username+' has been successfully registered')
    return render(request,'authentication/registration.html',{'form':form})

@unauthenticated_user
def login_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
            
        if user is not None:
            login(request,user)
            return redirect('test')
        else:
            messages.info(request,'Username or password is incorrect')


    return render(request,'authentication/login.html',{})

def logout_view(request):
    logout(request)
    return redirect('login')
    
    
    # template_name='authentication/registration.html'
    # success_url=reverse_lazy('login')
def test_view(request):
    return render(request,'authentication/test.html',{})

def customer_view(request):
    query=Customer.objects.all()
    return render(request,'authentication/customer.html',{'customer_list':query})


def dashboard(request):
    customers=Customer.objects.all()
    orders=Order.objects.all()
    total_customers=customers.count()
    total_orders=orders.count()
    delivered=orders.filter(status='Delivered').count()
    pending=orders.filter(status='Pending').count()
    context={'customers':customers,'orders': orders,'total_customers':total_customers,'total_orders':total_orders,'delivered':delivered,
    'pending':pending}
    return render(request,'authentication/dashboard.html',context)


def order_form(request):
    submitted=False
    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('orderform?submitted=True')
    else:
        form=OrderForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request,'authentication/order_form.html',{'submitted':submitted,'form':form})


def order_update(request,order_id):
    order=Order.objects.get(id=order_id)
    form=OrderForm(request.POST or None,instance=order)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request,'authentication/order_update.html',{'form':form,'order':order})




def order_delete(request, order_id):
    order = Order.objects.get(id=order_id)
    if request.method == "POST":
        order.delete()
	
        return redirect('dashboard')

    context = {'item':order}
    return render(request, 'authentication/order_delete.html', context)
        


