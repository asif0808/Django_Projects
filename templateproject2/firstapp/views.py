from django.shortcuts import render
import datetime
from templates import firstapp
def greet(request):
     date=datetime.datetime.now()
     hrs=int(date.strftime("%H"))
     s='very very '
     if(hrs<=12):
         s+="Good Morning"
     elif(hrs>12 and hrs<=16):
         s+="Good Afternoon"
     elif(hrs>16 and hrs<=21):
         s+="Good Evening"
     else:
        s+="Good Night"
     my_data={'msg':s,'time':date}
     return render(request,'firstapp/first.html',context=my_data)
