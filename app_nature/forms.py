from django import forms
from django.forms import ModelForm
from .models import posts

class City_Form(forms.Form):
    name_of_city = forms.CharField(label='Mesto, Dedina')

class UploadPost(forms.Form):
    #class Meta:
    #    model = posts
    #    fields = ['image', 'description', 'author']
    image = forms.ImageField()
    description = forms.CharField(widget=forms.Textarea)