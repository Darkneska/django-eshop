from django.shortcuts import HttpResponse
from django.shortcuts import render
from .models import *


def homepage(request):
    return render(request, 'homepage/home.html', {})


def shop(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'homepage/shop.html', context)


def reservation(request):
    return render(request, 'homepage/reservation.html', {})


def about(request):
    return render(request, 'homepage/about.html', {})


def detail(request, slug):
    product = Product.objects.get(slug=slug)
    return render(request, 'homepage/detail.html', {'data': product})


def bag(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {'items': items, 'order': order}
    return render(request, 'account/bag.html', context)


# def checkout(request):
#     if request.user.is_authenticated:
#         customer = request.user.customer
#         order, created = Order.objects.get_or_create(customer=customer, complete=False)
#         items = order.orderitem_set.all()
#     else:
#         items = []
#         order = {'get_cart_total': 0, 'get_cart_items': 0}
#
#     context = {'items': items, 'order': order}
#     return render(request, 'account/checkout.html', context)
