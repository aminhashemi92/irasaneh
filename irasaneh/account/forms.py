from django.contrib.auth import get_user_model
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Company, Code
from django import forms
class UserAdminCreationForm(UserCreationForm):
    """
    A Custom form for creating new users.
    """
    class Meta:
        model = get_user_model()
        fields = ['phone', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserAdminCreationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'input1'

        self.fields['phone'].widget.attrs.pop('autofocus', None)
        self.fields['phone'].widget.attrs['placeholder'] = '*********09'

    error_css_class = 'error'
        # widgets = {
        #     'phone': TextInput(attrs={
        #         'placeholder': "09123456789",
        #         }),
        # }


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['firstname', 'lastname', 'company', 'role', 'pic', 'sphone']
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['role'].widget.attrs['disabled'] = True

class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'logo', 'sphone',]



class CodeForm(ModelForm):
    number = forms.CharField(label='کد تایید',widget=forms.TextInput(attrs={'placeholder': '- - - - -', 'class': 'input1', }) )
    class Meta:
        model = Code
        fields = ('number', )
