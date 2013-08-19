from django.db import models
from datetime import datetime

class RequestLog(models.Model):
    path = models.CharField(max_length=256)
    time = models.DateTimeField(default=datetime.now())
