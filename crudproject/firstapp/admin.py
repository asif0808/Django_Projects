from django.contrib import admin
from firstapp.models import Company
class CompanyAdmin(admin.ModelAdmin):
    list_display=['date','name','company','email']
admin.site.register(Company,CompanyAdmin)
