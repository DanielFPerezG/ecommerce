from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from django.db.models import Q
from base.models import Product, Topic, Banner, User, Cart

from store.forms import UserForm, MyUserCreationForm

import json

# Create your views here.

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('store:home')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(email = email)
        except:
            messages.error(request, 'User does not exist')
        
        user = authenticate(request, email = email, password=password)

        if user is not None:
            login(request, user)
            return redirect('store:home')
        else:
            messages.error(request, 'Username or password is incorrect')

    context= {'page': page}
    return render(request, 'store/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('store:home')

def registerPage(request):
    page = 'register'
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    context = {'page': page, 'form':form}
    return render(request, 'store/login_register.html',context)

def home(request):
    topics = Topic.objects.all()
    banners = Banner.objects.all()
    cart, create = Cart.objects.get_or_create(user=request.user)
    products = Product.objects.order_by('-discount')

    productCarts = json.loads(cart.products)
    numberProductsCart = 0
    for productJson in productCarts:
        numberProductsCart += 1

    context = {
        'topics': topics,
        'banners': banners,
        'numberProductsCart': numberProductsCart,
        'products': products}
    return render(request, 'store/home.html', context)


def shopDetail(request,pk):
    product = Product.objects.get(id=pk)
    products = Product.objects.all()
    topics = Topic.objects.all()
    cart, create = Cart.objects.get_or_create(user=request.user)

    productCarts = json.loads(cart.products)
    numberProductsCart = 0
    for productJson in productCarts:
        numberProductsCart += 1

    context = {
        'products':products,
        'product':product,
        'topics':topics,
        'numberProductsCart':numberProductsCart
        }

    return render(request,'store/shopDetail.html', context)

def store(request):
    query = request.GET.get('q') if request.GET.get('q') != None else ''
    query_max_price = request.GET.get('q_max_price') if request.GET.get('q_max_price') != None else ''
    query_min_price = request.GET.get('q_min_price') if request.GET.get('q_min_price') != None else ''
    query_min_discount = request.GET.get('q_min_discount') if request.GET.get('q_min_discount') != None else ''
    order_by = request.GET.get('order_by', 'default_orders') 
    topics = Topic.objects.all()
    cart, create = Cart.objects.get_or_create(user=request.user)

    if query_max_price != '' and query_min_price != '': 
        products = Product.objects.filter(
            Q(price__gte=query_min_price) &
            Q(price__lte=query_max_price))
    elif query_max_price != '': 
        products = Product.objects.filter(
            Q(price__lte=query_max_price)
            )
    elif query_min_discount != '': 
        products = Product.objects.filter(
            Q(discount__gte=query_min_discount)
            )
        print('hpt')
    elif query:
        products = Product.objects.filter(
            Q(topic__name__icontains = query)|
            Q(name__icontains= query)|
            Q(bio__icontains= query)
        )
    else: 
        products = Product.objects.all()
    
    if order_by=="priceDiscount":
        products = products.order_by('priceDiscount')
    elif order_by=="-priceDiscount":
        products = products.order_by('-priceDiscount')
    elif order_by=="name":
        products = products.order_by('name')
    elif order_by=="-name":
        products = products.order_by('-name')
    elif order_by=="discount":
        products = products.order_by('-discount')
    elif order_by=="-discount":
        products = products.order_by('discount')
    
    paginator = Paginator(products, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    products = page_obj.object_list

    productCarts = json.loads(cart.products)
    numberProductsCart = 0
    for productJson in productCarts:
        numberProductsCart += 1


    context = {'products':products,'topics':topics,'query':query,'page_obj':page_obj,'products':products,'order_by':order_by,'numberProductsCart':numberProductsCart}
    return render(request, 'store/store.html', context)

@receiver(post_save, sender=User)
def create_cart(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(user=instance)


@login_required(login_url='login')
def addCart(request,pk):
    product = Product.objects.get(id=pk)
    cart, create = Cart.objects.get_or_create(user=request.user)
    newProductCarts = []
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        cart.add_product(product)
    productCarts = json.loads(cart.products)
    numberProductsCart = 0
    for productJson in productCarts :
        numberProductsCart += 1
        if int(productJson["id"]) == int(product.id):
            newProductCarts.append(productJson)
    numberProductsCart = json.dumps(numberProductsCart)
    newProductCarts = json.dumps(newProductCarts)

    data = {"json1": numberProductsCart, "json2": newProductCarts}
    data = json.dumps(data)
    return HttpResponse(data)

def viewCart(request):
    cart = Cart.objects.get(user=request.user)

    productCarts = json.loads(cart.products)
    numberProductsCart = 0
    subTotal = 0

    for productJson in productCarts:
        numberProductsCart += 1
        subTotal += productJson['total']
        if productJson['quantity'] == 0:
            cart.delete_product(productJson['id'])
            cart.save()
            productCarts.remove(productJson)


    numberProductsCart = json.dumps(numberProductsCart)
    productCart = cart.obtain_products()
    productCart_json = json.dumps(productCart)



    total = subTotal + 10000

    context = {'cart': cart, 'productCart': productCart, 'productCart_json': productCart_json,'numberProductsCart': numberProductsCart, 'subTotal': subTotal, 'total': total}
    return render(request, 'store/viewCart.html', context)

@csrf_exempt
def updateCart(request):
    cart = Cart.objects.get(user=request.user)
    productCart = cart.obtain_products()

    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        data = json.loads(request.body)


        for product in productCart:
            for i in data:
                if product["id"] == int(i["id"]):
                    product["quantity"] = int(i["quantity"])
            if product["quantity"] == 0:
                cart.delete_product(product["id"])

            product["total"] = product["price"]*product["quantity"]

        cart.products = productCart
        cart.products = json.dumps(cart.products)
        cart.save()
        productCart = json.dumps(productCart)
    return HttpResponse(productCart)

def deleteCart(request,pk):
    if request.method == 'POST':
        cart = Cart.objects.get(user=request.user)
        cart.delete_product(int(pk))
        cart.save()
    return redirect('store:viewCart')