from django.shortcuts import render
from templates import firstapp
def func(request):
    msg={'name':"Aasif"}
    return render(request,'firstapp/index.html',msg)
