import requests
BASE_URL= "http://127.0.0.1:8000/"
END_POINT="first"
resp=requests.get(BASE_URL+END_POINT)
print(type(resp))#<class 'requests.models.Response'>
print(resp)#<Response [200]>
print(type(resp.json))#<class 'method'>
print(resp.json())
data=resp.json()
print("Data from django applications is: ")
print('Employee No: ',data['eno'])
print('Employee Name: ',data['ename'])
print('Employee Address: ',data['eaddr'])
print('Employee Phone: ',data['ephone'])
