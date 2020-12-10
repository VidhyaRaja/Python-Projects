from django.db import models

# Create your models here.
class Site(models.Model):
    """Site model"""
    name = models.CharField(max_length=128)
    url = models.CharField(max_length=1024)
    image = models.ImageField(upload_to="images/")
    group = models.CharField(max_length=128)

class Group(models.Model):
    """Group model"""
    name = models.CharField(max_length=128)
    priority = models.IntegerField()
    
class Search(models.Model):
    """Search model"""
    name = models.CharField(max_length=128)
    image = models.CharField(max_length=1024, blank=True)
    urlPartBeforeKeywords = models.CharField(max_length=1024)
    urlPartAfterKeywords = models.CharField(max_length=1024)