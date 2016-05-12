from django.shortcuts import render

# Create your views here.
from django.http import *
from django.contrib import messages
from django.core.urlresolvers import reverse

from productes.models import Tipus_Producte

#Afagir Producte

def update_session(request, id_producte):

    if 'carro' not in request.session:
        request.session['carro'] ={}

    if id_producte not in request.session['carro']:
        qtat = 1
    else:
        qtat = request.session['carro'][id_producte]+1
    request.session['carro'].update({id_producte:qtat})

    messages.add_message(request, messages.SUCCESS, 'El producte ha sigut afegit correctament')
    return HttpResponseRedirect(reverse('producte:veure_productes') )

#Comandes

def veure_comande(request):
    if 'carro' not in request.session:
        request.session['carro'] = {}

    tipus = Tipus_Producte.objects.all()
    #comandes = Comanda.objects.all()
    comandes =request.session['carro']
    return render(request, 'comandes/index.html', {'comandes': comandes, 'tipus': tipus})

def esborra_carro(request):
    request.session['carro']={}
    return HttpResponseRedirect(reverse('producte:veure_productes'))