from django.shortcuts import render
from firstapp.forms import StudentForm
from templates import firstapp
def Student_form(request):
    submitted=False
    sname=''
    if(request.method=='POST'):
        form=StudentForm(request.POST)
        if form.is_valid():
            print('Form validation successfull....')
            print('Name: ',form.cleaned_data['name'])
            print('marks: ',form.cleaned_data['marks'])
            sname=form.cleaned_data['name']
            submitted=True
    form=StudentForm()
    mydict={'form':form,'sname':sname,'submitted':submitted}
    return render(request,'firstapp/input.html',mydict)
