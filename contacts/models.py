from django.db import models
from django.db.models.fields.related import OneToOneField

# Create your models here.
class ContactDetail(models.Model):
    email=models.CharField(max_length=50)
    jabber=models.CharField(max_length=50)
    skype=models.CharField(max_length=50)
    other = models.CharField(max_length=256)
    
class Contact(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birthdate = models.DateTimeField()
    bio = models.CharField(max_length=256)
    contactdetails=OneToOneField(ContactDetail, primary_key=True)  

    