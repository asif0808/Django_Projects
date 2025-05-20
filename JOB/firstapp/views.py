from django.shortcuts import render
from templates import firstapp
from firstapp.models import HydJobs,PuneJobs,BangJobs
def fun(request):
    return render(request,'firstapp/index.html')
def hyd(request):
    jobs_list=HydJobs.objects.all()
    mydict={'jobs_list':jobs_list}
    return render(request,'firstapp/hyd.html',mydict)
def pune(request):
    jobs_list=PuneJobs.objects.all()
    mydict={'jobs_list':jobs_list}
    return render(request,'firstapp/pune.html',mydict)
def bang(request):
    jobs_list=BangJobs.objects.all()
    mydict={'jobs_list':jobs_list}
    return render(request,'firstapp/bang.html',mydict)
