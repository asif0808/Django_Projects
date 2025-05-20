from django.shortcuts import render
from templates import firstapp
def wish(request):
    return render(request,'firstapp/home.html')
def marks(request):
    print(request.COOKIES)
    ename=request.GET['name']
    response= render(request,'firstapp/marks.html',{'name':ename})
    response.set_cookie('name',ename)
    return response
def age(request):
    print(request.COOKIES)
    ename=request.COOKIES['name']
    emarks=request.GET['marks']
    response= render(request,'firstapp/age.html',{'name':ename})
    response.set_cookie('marks',emarks)
    return response
def result_view(request):
    print(request.COOKIES)
    ename=request.COOKIES['name']
    emarks=request.COOKIES['marks']
    eage=request.GET['age']
    return render(request,'firstapp/result.html',{'name':ename,'marks':emarks,'age':eage})
