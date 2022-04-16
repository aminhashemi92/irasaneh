from django.contrib.auth import get_user_model
from django.forms import ModelForm
from .models import ContactUs
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field

class ContactUsForm(ModelForm):
        class Meta:
            model = ContactUs
            fields = ['firstname','lastname','title','description','role','mphone']

        def __init__(self, *args, **kwargs):
            super(ContactUsForm, self).__init__(*args, **kwargs)
            for visible in self.visible_fields():
                visible.field.widget.attrs['class'] = 'contactus'

            self.fields['description'].widget.attrs.update({
                'rows': '5'})
        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #     self.helper = FormHelper()
        #     self.helper.layout = Layout(Field(('firstname'), css_class="hello"),)
