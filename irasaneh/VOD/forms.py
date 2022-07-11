from django import forms
from .models import *
from django.forms import HiddenInput

class AdVideoForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(AdVideoForm, self).__init__(*args, **kwargs)
    #     self.fields['owner'].widget.attrs['disabled'] = True

    class Meta:
        model = AdVideo
        exclude = ('owner',)
        # fields = '__all__'
        # widgets={'owner': HiddenInput()}


class AdBoxForm(forms.ModelForm):
    class Meta:
        model = AdBox
        exclude = ('videos_list',)

    # def save(self):
    #     data = self.cleaned_data
    #     videos = data['videos']
    #     video_id_list = list(videos.values_list('id', flat=True))
    #     orders = data['order']
    #     orders_list = map(int, orders.split('-'))
    #     z = [x for _,x in sorted(zip(orders_list,video_id_list))]
    #     video_play_list = ','.join(map(str, z))
    #     print(video_play_list)


class AdEventForm(forms.ModelForm):
    class Meta:
        model = AdEvent
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AdEventForm, self).__init__(*args, **kwargs)
        self.fields['startDate'].widget.attrs.update({'id': 'date1', 'autocomplete':'off'})



class AdVideoFormCustomer(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(AdVideoForm, self).__init__(*args, **kwargs)
    #     self.fields['owner'].widget.attrs['disabled'] = True

    class Meta:
        model = AdVideo
        exclude = ('owner','company','status','condition',)
        # fields = ('name','type','video',)
        # widgets={'owner': HiddenInput()}
