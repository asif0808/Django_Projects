from django.shortcuts import render
from django.http import HttpResponse
def morning(request):
    s="Hello There !! Good Morning"
    return HttpResponse(s)

def evening(request):
    s="Hello There, Good Evening"
    return HttpResponse(s)
