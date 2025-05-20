from django.shortcuts import render
from django.http import HttpResponse
def greet1(request):
    return HttpResponse('<h1>Hello From Greet1</h1>')
def greet2(request):
    return HttpResponse('<h1>Hello From Greet2</h1>')
def greet3(request):
    return HttpResponse('<h1>Hello From Greet3</h1>')
