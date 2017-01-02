

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User, Group

from .models import Customer, AdminBranch, Admin
from .forms import SignUpCustomerForm

import random

def homepage(request):
    pass



def login_user(request):
    error = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print('after post')
        user = authenticate(username=username, password=password)
        if user is not None:
            print('in user if')
            login(request, user)
            group = Group.objects.get(name='Cashier')
            if group in request.user.groups.all():
                return redirect(reverse('SignUpCustomer'))
            else:
                return redirect(reverse('TestView', args={username}))
        else:
            print('in error')
            error = 'wrong username or password'
    context = {'error':error}
    return render(request, 'login.html', context)



@login_required()
def signup_customer(request):
    group = Group.objects.get(name='Cashier')
    if group not in request.user.groups.all():
        return redirect(reverse(''))
    if request.method == 'POST':
        form = SignUpCustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse(''))
    else:
        form = SignUpCustomerForm()
    context = {'form':form}
    return render(request, 'SignUpCustomer.html', context=context)





def signup_accountant(request):
    pass


def signup_branchAdmin(request):
    pass


@login_required(login_url='/loginCustomer')
def profile_customer(request, id):
    customer = Customer.objects.get(number = id)
    context = {'customer':customer}
    return render(request, '', context= context)


@login_required(login_url='/loginCustomer')
def test(request, username):
    customer = Customer.objects.get(user__username=username)
    context = {'customer':customer}
    return render(request, 'Test.html', context=context)


def logout_customer(request):
    logout(request)
    return redirect(reverse('LoginCustomer'))

