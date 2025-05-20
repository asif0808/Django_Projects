from django.shortcuts import render
from templates import firstapp
from firstapp.forms import NameForm,AgeForm,CourseForm
def name_view(request):
    form=NameForm()
    return render(request,'firstapp/main.html',{'form':form})
def age_view(request):
    name=request.GET['name']
    request.session['name']=name  #setting session
    form=AgeForm()
    return render(request,'firstapp/age.html',{'form':form,'name':name})
def course_view(request):
    age=request.GET['age']
    request.session['age']=age
    name=request.session['name']
    form=CourseForm()
    return render(request,'firstapp/course.html',{'form':form,'name':name,'age':age})
def results_view(request):
    name=request.session['name']
    age=request.session['age']
    course=request.GET['course']
    request.session['course']=course
    return render(request,'firstapp/results.html',{'name':name,'age':age,'course':course})
