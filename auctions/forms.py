from django.forms import ModelForm
from django import forms
from .models import *

# class NewForm(forms.Form):
#     title = forms.CharField(label="Title", required=True, widget=forms.TextInput(attrs={"placeholder" : "Title", "class" : "form-control"}))
#     description =  forms.CharField(label="Description", required = True, widget=forms.Textarea(attrs={"placeholder" : "description", "class" : "form-control"} ))


# class NewForm_two(forms.Form):
#     number = forms.IntegerField(label= False, required=True, widget=forms.NumberInput(attrs={"placeholder" : "Number", "class" : "form_number form-control" }) )
#     image = forms.ImageField(label= False )


class UploadForm(ModelForm):

    class Meta():
        model = Listing
        fields = "__all__"
        labels = {
            "title" : "",
            "description" : "",
            "bid" : "",
            "image" : ""      
        }


        widgets= {
            "title" : forms.TextInput(attrs={"class" : "form-control", "placeholder" : "Title"}),
            'description' : forms.Textarea(attrs={"class" : "form-control", "placeholder" : "Description"}),
            'bid' : forms.NumberInput(attrs={"class" : "form-control form_number", "placeholder" : "Price"}),
            "category" : forms.Select(attrs={"class" : "form-control"})
        }

class BidForm(ModelForm):
    class Meta():
        model = Listing
        fields = ["bid"]
        widgets = {
            "bid" : forms.NumberInput(attrs={"class" : "form-control form_number"})
        }