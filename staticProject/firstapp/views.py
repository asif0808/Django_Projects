from django.shortcuts import render
from templates import firstapp
def wish(request):
    msg='Good Morning'
    mydict={'greet':msg}
    return render(request,'firstapp/one.html',mydict)
