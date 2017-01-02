from .models import Customer

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

import random


class SignUpCustomerForm(forms.Form):
    first_name = forms.CharField(max_length=100, label='نام')
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def save(self):
        first_name = self.cleaed_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        email = self.cleaned_data('email')
        password = self.cleaned_data.get('password')
        while(True):
            try:
                number = random.randint(1000000, 9999999)
                user = User.objects.create_user(username=number, password=password, email=email, first_name=first_name,
                                                last_name=last_name)
                user.save()
                break
            except:
                pass
        customer = Customer()
        customer.user = user
        customer.number = number
        customer.save()
        group = Group.objects.get(name='Customer')
        group.user_set.add(user)