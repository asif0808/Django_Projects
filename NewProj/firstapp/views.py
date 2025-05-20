from django.shortcuts import render
from templates import firstapp
def greet(request):
    mydict={'name':'Aasif'}
    return render(request,'firstapp/one.html',mydict)
