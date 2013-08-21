from django.db import models
from cupstest.settings import MEDIA_URL
   
class Contact(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birthdate = models.DateTimeField()
    bio = models.CharField(max_length=256)
    photo = models.ImageField("Photo", upload_to="images/", blank=True, null=True)
    
    #Contacts...
    email=models.EmailField(max_length=254, default='')
    jabber=models.CharField(max_length=50, default='')
    skype=models.CharField(max_length=50, default='')
    other = models.CharField(max_length=256, default='')
   
    def __unicode__(self):
        return unicode(self.name + ' '+ self.surname)
    
    