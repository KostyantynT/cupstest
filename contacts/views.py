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

class UpdateContactView(generic.UpdateView):
    model = Contact
    template_name = 'contacts/edit.html'
    form_class = ContactForm