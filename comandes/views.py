from django.shortcuts import render

# Create your views here.
from django.http import *
from django.contrib import messages
from django.core.urlresolvers import reverse

from productes.models import Tipus_Producte, Producte

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
    tipus = Tipus_Producte.objects.all()

    if 'carro' not in request.session:
        request.session['carro'] = {}

    ##comandes =request.session['carro']

    ui_carro = []
    for id in request.session['carro']:
        ui_carro.append( { 'producte': Producte.objects.get( id_producte = id ),
                           'quantitat': request.session['carro'][id],
                         }
                        )

    return render(request, 'comandes/index.html', {'ui_carro': ui_carro, 'tipus': tipus})

def esborra_carro(request):
    del request.session['carro']
    return HttpResponseRedirect(reverse('producte:veure_productes'))

def esborra_linia(request, id_producte):
    request.session.modified = True
    producte = request.session['carro']
    del producte[id_producte]
    return HttpResponseRedirect(reverse('comande:veure_comande'))
