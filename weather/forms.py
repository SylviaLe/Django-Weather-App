from django.forms import ModelForm, TextInput
from .models import *

class CitiesForm(ModelForm):
    class Meta:
        model = Cities
        fields = ['name']
        widgets = {'name': TextInput(attrs={'class': 'input', 'placeholder':'City Name'})}