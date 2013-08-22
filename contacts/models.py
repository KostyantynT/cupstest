from django.db import models
from cupstest.settings import MEDIA_URL
   
class Contact(models.Model):
    name = models.CharField("Name",max_length=50)
    surname = models.CharField("Last name", max_length=50)
    birthdate = models.DateTimeField("Date of birth")
    bio = models.CharField("Bio", max_length=256)
    photo = models.ImageField("Photo", upload_to="images/", blank=True, null=True)
    
    #Contacts...
    email=models.EmailField("Email", max_length=254, default='')
    jabber=models.CharField("Jabber", max_length=50, default='')
    skype=models.CharField("Skype", max_length=50, default='')
    other = models.CharField("Other contacts", max_length=256, default='')
   
    def __unicode__(self):
        return unicode(self.name + ' '+ self.surname)
    
    