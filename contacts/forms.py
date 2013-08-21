from django import forms
from contacts.models import Contact

class ContactForm(forms.ModelForm):
    picture = forms.FileField(
            label = 'Select a picture',
            help_text='max. 4 megabytes'
            )
    class Meta:
        model = Contact
        
    def __init__(self, *args, **kwargs):
        if kwargs.get('instance'):
            name = kwargs['instance'].name
            surname = kwargs['instance'].surname
            birthdate = kwargs['instance'].birthdate
            bio = kwargs['instance'].bio
            contactdetails = kwargs['instance'].contactdetails
            #picture = kwargs['instance'].picture
        return super(ContactForm, self).__init__(*args, **kwargs)
    