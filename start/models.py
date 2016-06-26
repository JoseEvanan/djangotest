from django.db import models
from datetime import datetime 
# Create your models here.
class data(models.Model):
    value = models.CharField(max_length=9, blank=True, null=True)
    date = models.DateTimeField(default=datetime.now, blank=True)