from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Component(models.Model):
    nom= models.CharField(max_length=100)
    caracteristiques = models.TextField()
    imatge = models.ImageField(max_length=200, upload_to='components')
