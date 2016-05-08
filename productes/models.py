# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Tipus_Producte(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)

    def __str__(self):
        return '%s' % (self.nom)

class Marca_Producte(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)

    def __str__(self):
        return '%s' % (self.nom)

class Producte(models.Model):
    id_producte = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=200)
    marca = models.ForeignKey('Marca_Producte')
    tipus = models.ForeignKey('Tipus_Producte')
    caracteristiques = models.TextField(null=True, blank=True)
    restriccio = models.TextField(null=True, blank=True)
    imatge = models.ImageField(max_length=200, upload_to='productes')
    preu = models.DecimalField(max_digits=7,decimal_places=2, help_text="preu producte")
    stock = models.IntegerField()
