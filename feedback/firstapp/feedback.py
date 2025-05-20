from django import forms
from django.core.exceptions import ValidationError
def feedlen(val):
    print("starting feedback func..")
    if len(val)<10:
        raise forms.ValidationError("please provide atleast 10 characters")
def namelen(val):
    print("starting namelen func...")
    if len(val)<3:
        raise forms.ValidationError("Name should contain 3 or more characters")
class Feedbackform(forms.Form):
    name=forms.CharField(validators=[namelen],widget=forms.TextInput(attrs={'placeholder':'Enter Your Name','style':'border-color:blue;'}))
    Roll_no=forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'Enter Your Roll no.','style':'border-color:blue;'}))
    marks=forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'Enter Your Marks','style':'border-color:blue;'}))
    feedback=forms.CharField(validators=[feedlen],widget=forms.Textarea(attrs={"rows":"5",'placeholder':'Minimum 20 Characters','style':'border-color:black;'}))
    # def clean(self):
    #     cleaned_data=super().clean()
    #     name=cleaned_data['name']
    #     Roll_no=cleaned_data['Roll_no']
    #     marks=cleaned_data['marks']
    #     feedback=cleaned_data['feedback']
        # if len(name)<3:
        #     raise ValidationError("Wrong Name provided")
        # if Roll_no<=0:
        #     raise ValidationError("RollNO wrong")
