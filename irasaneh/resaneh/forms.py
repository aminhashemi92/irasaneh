from django import forms
from .models import Resaneh
class LocationForm(forms.ModelForm):
    class Meta:
   	 model = Resaneh
   	 fields = ['location']
