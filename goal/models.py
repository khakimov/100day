#coding: utf-8
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Goal(models.Model):
    choice = models.CharField(max_length=400)
    user = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.choice


class Report(models.Model):
    message = models.TextField()
    publication_date = models.DateField()
    user = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.message
