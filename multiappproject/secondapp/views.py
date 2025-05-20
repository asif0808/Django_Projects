from django.shortcuts import render
from django.http import HttpResponse
def wish2(request):
    return HttpResponse('Hello this is from secondapp views')
