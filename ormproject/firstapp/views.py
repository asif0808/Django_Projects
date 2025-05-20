from django.shortcuts import render
from templates import firstapp
def first_view(request):
    return render(request,'firstapp/first.html')
