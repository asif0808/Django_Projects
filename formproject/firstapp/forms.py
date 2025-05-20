from django import forms
from django.core.exceptions import ValidationError
class StudentForm(forms.Form):
    name=forms.CharField()
    marks=forms.CharField()
