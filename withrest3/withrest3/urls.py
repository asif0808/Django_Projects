"""
URL configuration for withrest3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from firstapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.EmployeeApiView.as_view()),
    path('create/', views.EmployeeCreateView.as_view()),
    #path('api/<int:pk>/', views.EmployeeRetrieveView.as_view()), #use this then we dont have to use lookup_field
#    below statement works only if we use lookup_field in views.py
   path('api/<int:id>/', views.EmployeeRetrieveView.as_view()),
   path('update/<int:id>/', views.EmployeeUpdateView.as_view()),
   path('delete/<int:id>/', views.EmployeeDeleteView.as_view()),
   #all at one url
   # path('api/<int:pk>/', views.EmployeeAllView.as_view(), name='item-detail'),
]
2
