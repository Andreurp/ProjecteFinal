from __future__ import unicode_literals

from django.db import models
from components.models import Component
from django.contrib.auth.models import User

# Create your models here.
class Linia(models.Model):
    id_Linia = models.AutoField(primary_key=True)
    id_comanda = models.ForeignKey('Comanda')
    id_component = models.ForeignKey('Component')
    quantitat = models.IntegerField()
    descompte = models.DecimalField(max_digits=4, decimal_places=1, default=0, help_text="descompte")

class Comanda(models.Model):
    num_comanda = models.AutoField(primary_key=True)
    data = models.DateField()
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
    estat = models.CharField(max_length=1, choices=Estat_Comanda, help_text="Estat_Comanda")
