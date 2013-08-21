# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from contacts.models import Contact
from contacts.forms import ContactForm
from django.views import generic

class IndexView(generic.DetailView):
    model = Contact
    template_name='contacts/index.html'
    
    def get_queryset(self):
        if self.kwargs.get("pk") is None:
            self.kwargs["pk"]=1
        return Contact.objects.filter(pk=self.kwargs["pk"])

class UpdateContactView(generic.UpdateView):
    model = Contact
    template_name = 'contacts/edit.html'
    form_class = ContactForm