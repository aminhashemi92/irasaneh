from django.contrib.auth import get_user_model
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Company

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


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['firstname', 'lastname', 'company', 'role', 'pic', 'sphone', 'mphone']


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'logo', 'sphone', 'mphone']