from django.shortcuts import render
from django.http import HttpResponse
def display(request):
    s='Welcom to Django classes'
    return HttpResponse(s)
