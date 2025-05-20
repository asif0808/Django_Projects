from django.shortcuts import render
from templates import firstapp
def page_count_view(request):
    print("cookies from client: ",request.COOKIES)
    count=int(request.COOKIES.get('count',0))
    count+=1
    response=render(request,'firstapp/first.html',{'count':count})
    response.set_cookie('count',count)
    return response
