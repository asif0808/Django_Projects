from django.shortcuts import render
from templates import firstapp
from firstapp.forms import ItemForm
def main_view(request):
    return render(request,'firstapp/main.html')
def add_view(request):
    form=ItemForm()
    response=render(request,'firstapp/additem.html',{'form':form})
    if request.method=='POST':
        form=ItemForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['product_name']
            quantity=form.cleaned_data['quantity']
        response.set_cookie(name,quantity)
        #print(request.COOKIES)
    return response
def set_view(request):
    return render(request,'firstapp/show.html')
