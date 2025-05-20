from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from templates import firstapp,registration
def main_view(request):
    return render(request,'firstapp/main.html')
def home_view(request):
    return render(request,'firstapp/home.html')
@login_required
def java_view(request):
    return render(request,'firstapp/java.html')
@login_required
def python_view(request):
    return render(request,'firstapp/python.html')
@login_required
def aptitude_view(request):
    return render(request,'firstapp/aptitude.html')
def logout_view(request):
    return render(request,'firstapp/logout.html')
from firstapp.forms import SignUpForm
from django.http import HttpResponseRedirect
def signup_view(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        user=form.save()
        user.set_password(user.password) #to hash the set_password
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'firstapp/signup.html',{'form':form})
