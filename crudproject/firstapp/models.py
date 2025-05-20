from django.db import models
class Company(models.Model):
    date=models.DateField()
    name=models.CharField(max_length=32)
    company=models.CharField(max_length=32)
    email=models.EmailField()
