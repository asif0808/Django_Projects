from django import forms
class ItemForm(forms.Form):
    product_name=forms.CharField()
    quantity=forms.IntegerField()
