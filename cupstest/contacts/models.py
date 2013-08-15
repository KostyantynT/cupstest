from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birthdate = models.DateTimeField()
    bio = models.CharField(max_length=256)
    contacts = models.CharField(max_length=256)
