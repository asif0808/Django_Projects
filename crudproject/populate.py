import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crudproject.settings')
import django
django.setup()
from firstapp.models import Company
from faker import Faker
fake=Faker()
def populate(n):
    for i in range(n):
        fdate=fake.date()
        fname=fake.name()
        fcompany=fake.company()
        femail=fake.email()
        company_records=Company.objects.get_or_create(date=fdate,name=fname,company=fcompany,email=femail)
n=int(input("enter number of records: "))
populate(n)
print(f"{n} records inserted successfully")
