from django import forms

from contacts.models import Contact
# 
class ContactForm(forms.ModelForm):
    success_url = '/contacts/'
    photo = forms.ImageField(label='Photo',required=False, error_messages = {'invalid':"Image files only"}, widget=forms.FileInput)
    bio = forms.CharField(widget=forms.Textarea()) 
    other = forms.CharField(label='Other contacts', widget=forms.Textarea())
    class Meta: # model must be in the Meta class
        model = Contact
        fields=("name","surname","birthdate","photo", "email","jabber", "skype","other", "bio")