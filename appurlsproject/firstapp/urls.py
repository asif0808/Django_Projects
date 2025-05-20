from django.urls import path
from . import views
urlpatterns = [
    path('first/', views.greet1),
    path('second/', views.greet2),
    path('third/', views.greet3),

]
