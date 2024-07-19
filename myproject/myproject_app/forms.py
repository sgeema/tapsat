from django import forms
from django.contrib.auth.models import User
from .models import Shop, Shoe, Customer

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

class ShopRegisterForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['name', 'address', 'brands']

class ShoeForm(forms.ModelForm):
    class Meta:
        model = Shoe
        fields = ['name', 'brand', 'size', 'color', 'quantity', 'image']

class CustomerRegisterForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['shoe_size']
