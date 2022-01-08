from django.shortcuts import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, 'homepage/home.html', {})
