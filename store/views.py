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


def detail(request):
    return render(request, 'homepage/detail.html', {})
