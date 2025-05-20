from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from firstapp.serializers import NameSerializer
class TestApiView(APIView):
    def get(self,request,*args,**kwargs):
        colors=['RED','YELLOW','GREEN','BLUE']
        #response class is responsible to convert python object to json data
        return Response({'msg':'Rise of the haf moon','colors':colors})
    def post(self,request,*args,**kwargs):
        serializer = NameSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            msg = 'Hello {}, happy new year!!!!!'.format(name)
            return Response({'msg':msg})
        else:
            return Response(serializer.errors,status=400)
    def put(self,request,*args,**kwargs):
        return Response({'msg':'This response from PUT method APIView'})
    def patch(self,request,*args,**kwargs):
	    return Response({'msg':'This response from PATCH method APIView'})
    def delete(self,request,*args,**kwargs):
        return Response({'msg':'This response from DELETE method APIView'})
