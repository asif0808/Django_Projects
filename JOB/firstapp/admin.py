from django.contrib import admin
from firstapp.models import HydJobs,PuneJobs,BangJobs
class HydJobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']
admin.site.register(HydJobs,HydJobsAdmin)
class PuneJobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']
admin.site.register(PuneJobs,PuneJobsAdmin)
class BangJobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']
admin.site.register(BangJobs,BangJobsAdmin)
