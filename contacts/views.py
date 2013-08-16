# Create your views here.
from django.shortcuts import render

from contacts.models import Contact

def index(request):
    contact = Contact.objects.get(pk=1)
    return render(request, 'contacts/index.html', {'contact':contact})