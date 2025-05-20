from django.shortcuts import render
import json
from django.http import HttpResponse,JsonResponse
def main_view(request):
    my_data={
    'eno':101,
    'ename':'aasif',
    'eaddr':'gkp',
    'ephone':4382
    }
    #providing normal dict data as a response
    #resp='<h1>Employee Number: {} <br>Employee Name: {} <br>Employee Address: {} <br>Employee phone: {} <br></h1>'.format(my_data['eno'],my_data['ename'],my_data['eaddr'],my_data['ephone'])
    # #passing as json data
    # json_data=json.dumps(my_data)
    # return HttpResponse(json_data,content_type='application/json')
    #passing directly as json_data
    return JsonResponse(my_data)
