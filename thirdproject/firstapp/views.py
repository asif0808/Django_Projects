from django.shortcuts import render
import datetime
from django.http import HttpResponse
# To get the current time in particular, you can use the strftime() method and pass into it
# the string ”%H:%M:%S” representing hours, minutes, and seconds.
def display(request):
    date=datetime.datetime.now()
    s='<h1>Good Morning</h1><hr>'
    s+='The system time is : '
    s+=str(date)
    return HttpResponse(s)
def dynamicDisplay(request):
     date=datetime.datetime.now()
     hrs=int(date.strftime("%H"))
     s="<h1>Hello Everyone, </h1>"
     if(hrs<=12):
         s+="<h1>Good Morning</h1><hr>"
     elif(hrs>12 and hrs<=16):
         s+="<h1>Good Afternoon</h1><hr>"
     elif(hrs>16 and hrs<=21):
         s+="<h1>Good Evening</h1><hr>"
     else:
        s+="<h1>Good Night</h1><hr>"
     s+='The System time is '+str(date)+''
     return HttpResponse(s)
