import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'JOB.settings')
import django
django.setup()
from faker import Faker
from firstapp.models import HydJobs,PuneJobs,BangJobs
from random import *
fake=Faker()
def phonenumbergen():
    p=randint(7,9)
    num=''+str(p)
    for i in range(9):
        num+=str(randint(0,9))
    return int(num)
def populate(n):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_element(elements=('Project Manager','Teacher','Team Lead','Media Manager'))
        feligibility= fake.random_element(elements=('Btech','MCA','PhD','MBBS'))
        faddress=fake.address()
        femail=fake.email()
        fphonenumber=phonenumbergen()
        if(loc=='hyd'):
            hyd_jobs_record=HydJobs.objects.get_or_create(date=fdate,
            company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,email=femail,phonenumber=fphonenumber,)
        if(loc=='pune'):
            pune_jobs_record=PuneJobs.objects.get_or_create(date=fdate,
            company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,email=femail,phonenumber=fphonenumber,)
        if(loc=='banglore'):
            bang_jobs_record=BangJobs.objects.get_or_create(date=fdate,
            company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,email=femail,phonenumber=fphonenumber,)
n=int(input('Enter number of records: '))
loc=input('enter location(hyd/pune/banglore): ')
populate(n)
print(f"{n} records are inserted successfully")
