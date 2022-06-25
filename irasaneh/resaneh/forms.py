from django import forms
from .models import Resaneh
from location_field.forms.plain import PlainLocationField
from django.forms import HiddenInput

class LocationForm(forms.ModelForm):
    class Meta:
        model = Resaneh
        fields = ['location']


class DigitalResanehFrom(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(DigitalResanehFrom, self).__init__(*args, **kwargs)
    #     self.fields['creator'].widget.attrs['disabled'] = True
    # def __init__(self, *args, **kwargs):
    #
    #     super(DigitalResanehFrom, self).__init__(*args, **kwargs)
    #     self.fields['creator'].initial = request.user
        # user = self.instance.user

    class Meta:
        model = Resaneh
        fields = ['creator', 'company', 'place','name', 'slug','owner', 'country', 'state', 'city', 'zone','address','location','nvisit','price','detail','point','status','code','connectionID','publish','industry','tag','category','is_digital','tvModel','tvSize','is_Androidbox','androidVersion','operatorNumber']
        widgets={'creator': HiddenInput()}
