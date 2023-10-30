from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from phonestore.forms import OrderForm, CustomerForm, CreateNewUser 
# Create your views here.
from .models import Phone, Customer, Order
from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import notLoggedUsers, allowedusers
from django.contrib.auth.models import Group
import requests
from django.conf import settings


@login_required(login_url='userlogin')
def dashboard(request):
    
    
    search = Customer.objects.all()
    name = None
    customer = Customer.objects.all()
    orders = Order.objects.all()
    phones= Phone.objects.all()
    total_orders = Order.objects.all().count()
    p_total_orders = Order.objects.filter(status ='pending').count()
    d_total_orders = Order.objects.filter(status ='delivred').count()
    i_total_orders = Order.objects.filter(status ='in progress').count()
    o_total_orders = Order.objects.filter(status ='Out of order').count()
    if 'search_name' in request.GET:
        name = request.GET['search_name']
        if name:
            #search = search.filter(author__icontains=title)
            search = search.filter(name__icontains=name)
            customer=search

    context ={
    'customer' : customer,
    'orders' : orders,
    'phones': phones,
    'total_orders' : total_orders,
    'p_total_orders' : p_total_orders,
    'd_total_orders' : d_total_orders,
    'i_total_orders' : i_total_orders,
    'o_total_orders' : o_total_orders,
    'custom':search,
    }

    return render(request, 'phonestore/dashboard.html',context )


def customer(request, slug):

    customer_id = Customer.objects.get(id = slug)
     
    orders = customer_id.order_set.all()
    nbr_orders = orders.count()
    searchFilter = OrderFilter(request.GET, queryset=orders)
    orders = searchFilter.qs
    context ={'customer_id': customer_id,
              'orders' : orders, 
              'nbr_orders':nbr_orders,
              'searchFilter':searchFilter,
              }
    
    return render(request,'phonestore/customer.html', context)



def phones(request):
    phones= Phone.objects.all()
    context = {
        'phones': phones,
    }


    return render(request, 'phonestore/phones.html',context)




def create(request):

    
     
    form = OrderForm
    if request.method == 'POST':
        
        form= OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    
    context = {
         'form': form
     }
    return render(request, 'phonestore/order_form.html', context)

def create_P(request, slug ):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('phone', 'status'), extra=1)
    customerid = Customer.objects.get(id = slug)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customerid)
    #form = OrderForm
    if request.method == 'POST':
        
        #form= OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customerid)

        if formset.is_valid():
            formset.save()
            return redirect('/')

    
    context = {
         'formset': formset,
         
     }
    return render(request, 'phonestore/order_form.html', context)

def update(request, slug):
     order = Order.objects.get(id=slug)
     form = OrderForm(instance=order)
     if request.method == 'POST':
        
        form= OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            
            return redirect('/')
             
     context = {
         'form': form
     }
     return render(request, 'phonestore/order_form.html', context)

def delete(request, slug):
     

    order = Order.objects.get(id=slug)
    if request.method == 'POST':
            order.delete()
            return redirect('/')

    context = {
         'order': order
     }
    return render(request, 'phonestore/delete_form.html', context)


# CRUD CUSTOMER
def create_C(request):
     
    form_c = CustomerForm
    if request.method == 'POST':
        
        form_c= CustomerForm(request.POST)
        if form_c.is_valid():
            form_c.save()
            return redirect('/')

    
    context = {
         'form_c': form_c
     }
    return render(request, 'phonestore/customer_form.html', context)

def update_C(request, slug):
     customer = Customer.objects.get(id=slug)
     form_c = CustomerForm(instance=customer)
     if request.method == 'POST':
        
        form_c= CustomerForm(request.POST, instance=customer)
        if form_c.is_valid():
            form_c.save()
            return redirect('/')
             
     context = {
         'form_c': form_c
     }
     return render(request, 'phonestore/customer_form.html', context)

def delete(request, slug):
     

    customer = Customer.objects.get(id=slug)
    if request.method == 'POST':
            customer.delete()
            return redirect('/')

    context = {
         'customer': customer
     }
    return render(request, 'phonestore/delete_form.html', context)





def register(request):
    if request.user.is_authenticated:
        
        messages.warning(request, 'Ops! User  already registred!')
        return redirect('dashboard')

    form = CreateNewUser()
    if request.method == 'POST':
        form=CreateNewUser(request.POST)
        if form.is_valid():
            recaptcha_response = request.POST.get('g-recaptcha-response')
            data = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
            }
            r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
            result = r.json()
            if result['success']:

                user=form.save()
                username = form.cleaned_data.get('username')
                # group = Group.objects.get(name='customer')
                # user.groups.add(group)
                messages.success(request, username + '  Created successfully!')
                return redirect('userlogin')
            else:

                messages.error(request, 'Invalid reCAPTCHA. Please try again.')

    context = {
         'form':form,
         'recaptcha_site_key':settings.GOOGLE_RECAPTCHA_SITE_KEY
     }
    return render(request, 'phonestore/register.html', context, )



def userlogin(request):
    if request.user.is_authenticated:
        
        messages.success(request, 'Ops! User already authenticated!')
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password )
        if user is not None:
            login(request, user)
            messages.success(request, '  loged successfully!')
            return redirect ('dashboard')
        else:
            messages.info(request, 'Wrong username or password Try again!')


    context = {
         
     }
    return render(request, 'phonestore/userlogin.html', context)

def userlogout(request):
    if request.user.is_authenticated:
        
        
        logout(request)
        messages.info(request, 'logout successfully!')
        return redirect ('userlogin')
    messages.warning(request, 'Ops! You should login first!')
    return redirect('dashboard')

@login_required(login_url='userlogin')
def profile(request):
    
    orders = request.user.customer.order_set.all()

    
    search = Customer.objects.all()
    name = None
    
    
    phones= Phone.objects.all()
    total_order = orders.filter().count()
    p_total_orders = orders.filter(status ='pending').count()
    d_total_orders = orders.filter(status ='delivred').count()
    i_total_orders = orders.filter(status ='in progress').count()
    o_total_orders = orders.filter(status ='Out of order').count()
    if 'search_name' in request.GET:
        name = request.GET['search_name']
        if name:
            #search = search.filter(author__icontains=title)
            search = search.filter(name__icontains=name)
            customer=search

    context ={
    
    'orders' : orders,
    'phones': phones,
    'total_order' : total_order,
    'p_total_orders' : p_total_orders,
    'd_total_orders' : d_total_orders,
    'i_total_orders' : i_total_orders,
    'o_total_orders' : o_total_orders,
    'custom':search,
    }
    return render(request, 'phonestore/profile.html',context, )


def profile_info(request):
    orders = request.user.customer.order_set.all()

    total_order = orders.filter().count()
    customer = request.user.customer
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        
        form= CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('profile_info')
             

    context = {
        'total_order': total_order,
        'form':form


    }
    
    return render(request, 'phonestore/profile_info.html',context, )
