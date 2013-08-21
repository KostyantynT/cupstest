from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.fields.related import OneToOneField
from cupstest.settings import MEDIA_URL

# Create your models here.
class ContactDetail(models.Model):
    email=models.EmailField(max_length=254)
    jabber=models.CharField(max_length=50)
    skype=models.CharField(max_length=50)
    other = models.CharField(max_length=256)
    
class Contact(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birthdate = models.DateTimeField()
    bio = models.CharField(max_length=256)
    contactdetails=OneToOneField(ContactDetail, primary_key=True)
    photo = models.ImageField("Photo", upload_to="images/", blank=True, null=True)
   
    def __unicode__(self):
        return unicode(self.name + ' '+ self.surname)
    
    def picture_url(self):
        return (MEDIA_URL + self.picture.url) if self.picture else None

    