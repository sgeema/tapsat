from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegisterForm, ShopRegisterForm, ShoeForm, CustomerRegisterForm
from .models import Shop, Shoe, Customer

def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            login(request, user)
            return redirect('shop_or_customer')
    else:
        user_form = UserRegisterForm()
    return render(request, 'shop/register.html', {'user_form': user_form})

def shop_or_customer(request):
    if request.method == 'POST':
        if 'shop' in request.POST:
            shop_form = ShopRegisterForm(request.POST)
            if shop_form.is_valid():
                shop = shop_form.save(commit=False)
                shop.owner = request.user
                shop.save()
                return redirect('add_shoe')
        elif 'customer' in request.POST:
            customer_form = CustomerRegisterForm(request.POST)
            if customer_form.is_valid():
                customer = customer_form.save(commit=False)
                customer.user = request.user
                customer.save()
                return redirect('shop_list')
    else:
        shop_form = ShopRegisterForm()
        customer_form = CustomerRegisterForm()
    return render(request, 'shop/shop_or_customer.html', {'shop_form': shop_form, 'customer_form': customer_form})

def add_shoe(request):
    if request.method == 'POST':
        shoe_form = ShoeForm(request.POST, request.FILES)
        if shoe_form.is_valid():
            shoe = shoe_form.save(commit=False)
            shoe.shop = request.user.shop
            shoe.save()
            return redirect('shop_detail', pk=request.user.shop.pk)
    else:
        shoe_form = ShoeForm()
    return render(request, 'shop/add_shoe.html', {'shoe_form': shoe_form})

def shop_list(request):
    shops = Shop.objects.all()
    return render(request, 'shop/shop_list.html', {'shops': shops})

def shop_detail(request, pk):
    shop = Shop.objects.get(pk=pk)
    shoes = Shoe.objects.filter(shop=shop)
    return render(request, 'shop/shop_detail.html', {'shop': shop, 'shoes': shoes})

