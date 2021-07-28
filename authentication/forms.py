from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import EmailInput
from .models import *



class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields='__all__'
     
    name=forms.CharField(max_length=120)
    phone=forms.DecimalField(max_digits=3,decimal_places=0)
    
    


class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields='__all__'



