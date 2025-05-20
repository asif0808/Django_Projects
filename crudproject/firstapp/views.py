from django.shortcuts import render,redirect
from firstapp.models import Company
from templates import firstapp
def main_view(request):
    total_data=Company.objects.all()
    mydict={'total_data':total_data}
    return render(request,'firstapp/main.html',mydict)
from firstapp.forms import CompanyForm
def insert_view(request):
    form=CompanyForm()
    if request.method=='POST':
        form=CompanyForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'firstapp/insert.html',{'form':form})
def delete_view(request,id):
    comp=Company.objects.get(id=id)
    comp.delete()
    return redirect('/')
def Update_view(request,id):
    comp=Company.objects.get(id=id)
    form=CompanyForm(instance=comp)
    if request.method=='POST':
        form=CompanyForm(request.POST,instance=comp)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'firstapp/update.html',{'form':form,'comp':comp})
