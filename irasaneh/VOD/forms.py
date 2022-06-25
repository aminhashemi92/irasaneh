from django import forms
from .models import *
from django.forms import HiddenInput

class AdVideoForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(AdVideoForm, self).__init__(*args, **kwargs)
    #     self.fields['owner'].widget.attrs['disabled'] = True

    class Meta:
        model = AdVideo
        fields = '__all__'
        widgets={'owner': HiddenInput()}


class AdBoxForm(forms.ModelForm):
    class Meta:
        model = AdBox
        fields = '__all__'

class AdEventForm(forms.ModelForm):
    class Meta:
        model = AdEvent
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AdEventForm, self).__init__(*args, **kwargs)
        self.fields['startDate'].widget.attrs.update({'id': 'date1', 'autocomplete':'off'})
