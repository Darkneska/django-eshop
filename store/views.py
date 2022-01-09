from django.shortcuts import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, 'homepage/home.html', {})


def contact(request):
    return render(request, 'homepage/contact.html', {})
