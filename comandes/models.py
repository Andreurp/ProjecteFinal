from __future__ import unicode_literals

from django.db import models
from components.models import Component

# Create your models here.
class Comanda(models.Model):
    num_comanda= models.IntegerField()
    #usuari = models.ForeignKey(User)
    components = models.ForeignKey(Component)
