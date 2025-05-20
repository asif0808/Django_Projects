from django.db import models
class Crud(models.Model):
    roll_no=models.IntegerField()
    name=models.CharField(max_length=30)
