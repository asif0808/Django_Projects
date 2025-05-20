from django.shortcuts import render
from templates import firstapp
from firstapp.models import Crud
def main_view(request):
    myd=Crud.objects.all()
    return render(request,'firstapp/one.html',{'mydict':myd})
