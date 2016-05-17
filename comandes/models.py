# encoding: utf-8

from __future__ import unicode_literals

from django.db import models
from productes.models import Producte
from django.contrib.auth.models import User

# Create your models here.
class Linia(models.Model):
    id_linia = models.AutoField(primary_key=True)
    id_comanda = models.ForeignKey('Comanda')
    id_producte = models.ForeignKey('productes.Producte')
    preu = models.DecimalField(max_digits=7, decimal_places=2)
    quantitat = models.IntegerField()
    descompte = models.DecimalField(max_digits=4, decimal_places=1, default=0, null=True, blank=True, help_text="descompte")
    def preu_linia(self):
        return self.quantitat*self.preu-(self.quantitat*self.preu-(self.descompte/100))

class Comanda(models.Model):
    id_comanda = models.AutoField(primary_key=True)
    data = models.DateField(auto_now=True)
    usuari = models.ForeignKey(User)
    Rebuda = 'R'
    Processant = 'P'
    Finalitazada = 'F'
    Entregada = 'E'
    Anulada = 'A'
    Estat_Comanda = ((Rebuda, 'Rebuda',),
                     (Processant, 'Processant',),
                     (Finalitazada, 'Finalitazada',),
                     (Entregada, 'Entregada',),
                     (Anulada, 'Anulada',)
                     )
    estat = models.CharField(max_length=1, choices=Estat_Comanda, default='R', help_text="Estat_Comanda")
