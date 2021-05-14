from django.forms import ModelForm, TextInput
from django.forms.fields import CharField
from .models import *
from django import forms


#####OPTION 1: NO database, use Form only
class CitiesForm(forms.Form):
    name = CharField(max_length=50, label="Name", widget=TextInput(attrs={'class': 'input', 'placeholder':'City Name'}))


#####OPTION 2: ModelForm, save to the database
# class CitiesForm(ModelForm):
#     class Meta:
#         model = Cities
#         fields = ['name']
#         widgets = {'name': TextInput(attrs={'class': 'input', 'placeholder':'City Name'})}