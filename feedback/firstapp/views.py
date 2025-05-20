from django.shortcuts import render
from templates import firstapp
from firstapp.feedback import Feedbackform
from django import forms
def feedback_form(request):
    submitted=False
    s=''
    if request.method=='POST':
        feed=Feedbackform(request.POST)
        if feed.is_valid():
            print("form submitted successfully")
            print("Name: ",feed.cleaned_data["name"])
            print("Marks: ",feed.cleaned_data["marks"])
            print("Feedback: ",feed.cleaned_data["feedback"])
            s=feed.cleaned_data["name"]
            submitted=True
    else:
        feed=Feedbackform()
    mydict={'feed':feed,'sname':s,'submitted':submitted}
    return render(request,'firstapp/feed.html',mydict)
