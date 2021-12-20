from django.shortcuts import HttpResponse
from django.shortcuts import render


def homepage(*args, **kwargs):
    return HttpResponse('<h1>Here will be main page</h1>')
