from firstapp.models import Employee
from firstapp.serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
class EmployeeApiView(ListAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
from rest_framework.generics import CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView#RetrieveUpdateDestroyAPIView
class EmployeeCreateView(CreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
class EmployeeRetrieveView(RetrieveAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    lookup_field='id'
class EmployeeUpdateView(UpdateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    lookup_field='id'
class EmployeeDeleteView(DestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    lookup_field='id'

#all at one url
# class EmployeeAllView(RetrieveUpdateDestroyAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer
