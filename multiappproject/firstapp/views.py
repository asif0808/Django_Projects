from django.shortcuts import render
from django.http import HttpResponse
def wish1(request):
    return HttpResponse('Hello This is from firstapp views')
