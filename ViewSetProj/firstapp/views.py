from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from firstapp.serializers import NameSerializer
class TestViewSet(ViewSet):
    def list(self,request):
        colors=['red','blue','white']
        return Response({'msg':'Happy holi'})
    def create(self,request):
        serializer=NameSerializer(data=request.data)
        if serializer.is_valid():
            name=serializer.data.get('name')
            msg='Hello {}, Happy new year'.format(name)
            return Response({'msg':msg})
        else:
            return Response(serializer.error,status=400)
    def retrieve(self,request,*args,**kwargs):
	    return Response({'msg':'This response from RETRIEVE method APIView'})
    def update(self,request,*args,**kwargs):
        return Response({'msg':'This response from UPDATE method APIView'})
    def partial_update(self,request,*args,**kwargs):
        return Response({'msg':'This response from PARTIAL_UPDATE method APIView'})
    def destroy(self,request,*args,**kwargs):
        return Response({'msg':'This response from DESTROY method APIView'})
