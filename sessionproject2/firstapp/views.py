from django.shortcuts import render
from templates import firstapp
from firstapp.forms import LoginForm
def form_view(request):
    form=LoginForm()
    return render(request,'firstapp/first.html',{'form':form})
def time_view(request):
    name=request.GET['name']
    #set the cookies to response
    response= render(request,'firstapp/time.html',{'name':name})
    response.set_cookie('name',name)
    return response
import datetime
def result(request):
    #case matters (case sensitive)
    name=request.COOKIES.get('name')
    time=datetime.datetime.now()
    return render (request,'firstapp/results.html',{'time':time,'name':name})
