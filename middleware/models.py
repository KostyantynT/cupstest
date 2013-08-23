from django.db import models

class RequestLog(models.Model):
    path = models.CharField(max_length=256)
    time = models.DateTimeField(auto_now=True)
