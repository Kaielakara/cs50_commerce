from django import forms
from .models import *

class NewForm(forms.Form):
    title = forms.CharField(label="Title", required=True, widget=forms.TextInput(attrs={"placeholder" : "Title", "class" : "form-control"}))
    description =  forms.CharField(label="Description", required = True, widget=forms.Textarea(attrs={"placeholder" : "description", "class" : "form-control"} ))


class NewForm_two(forms.Form):
    number = forms.IntegerField(label= False, required=True, widget=forms.NumberInput(attrs={"placeholder" : "Number", "class" : "form_number form-control" }) )
    image = forms.ImageField(label= False)