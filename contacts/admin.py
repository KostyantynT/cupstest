from django.contrib import admin
from contacts.models import Contact
from contacts.models import ContactDetail

admin.site.register(Contact)
admin.site.register(ContactDetail)