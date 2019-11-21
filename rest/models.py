from django.db import models

# Create your models here.
import datetime

class notes(models.Model):
    Title= models.CharField(max_length=150)
    Description = models.CharField(max_length=150)
    date_created =models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.Title