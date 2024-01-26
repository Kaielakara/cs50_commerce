from django import forms

class NewForm(forms.Form):
    title = forms.CharField(label="title", required= True)
    description =  forms.CharField(label="description", required = True)
    number = forms.IntegerField(required=True)
    image = forms.ImageField()