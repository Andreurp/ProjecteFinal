from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Tipus_Component(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)

class Component(models.Model):
    id_component = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=200)
    marca = models.CharField(max_length=100)
    tipus = models.ForeignKey('Tipus_Component')
    caracteristiques = models.TextField()
    restriccio = models.TextField()
    imatge = models.ImageField(max_length=200, upload_to='components')
    preu = models.DecimalField(max_digits=7,decimal_places=2, help_text="preu component")
    stock = models.IntegerField()
