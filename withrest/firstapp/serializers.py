from rest_framework import serializers
from firstapp.models import Employee
class EmployeeSerializer(serializers.Serializer):
    eno=serializers.IntegerField()
    ename=serializers.CharField(max_length=64)
    esal=serializers.FloatField()
    eaddr=serializers.CharField(max_length=64)#we should go for model serializers
# class EmployeeSerializer(serializers.ModelSerializer):
# class Meta:
#     model = Employee
#     fields=['eno','ename']
