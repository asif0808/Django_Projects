from django.shortcuts import render
from templates import firstapp
def wish(request):
    return render(request,'firstapp/greet.html')
