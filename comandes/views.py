from django.shortcuts import render, get_object_or_404

from django.http import *
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from productes.models import Tipus_Producte, Producte
from comandes.models import Comanda, Linia

#Afagir Producte en el carro

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

#Comanda actual

def veure_comande(request):
    tipus = Tipus_Producte.objects.all()

    if 'carro' not in request.session:
        request.session['carro'] = {}

    ##comandes =request.session['carro']

    ui_carro = []
    preu_comanda = 0
    for id in request.session['carro']:
        pr = Producte.objects.get(id_producte=id)
        qtat = request.session['carro'][id]
        preu_total = pr.preu*qtat
        preu_comanda+=preu_total
        ui_carro.append( { 'producte': pr,
                           'quantitat':qtat,
                           'preu_total':preu_total
                         }
                        )

    return render(request, 'comandes/index.html', {'ui_carro': ui_carro, 'preu_comanda': preu_comanda,'tipus': tipus})

def esborra_carro(request):
    #control per si esborren per GET
    if 'carro' in request.session:
        del request.session['carro']
    return HttpResponseRedirect(reverse('producte:veure_productes'))

def esborra_linia(request, id_producte):
    request.session.modified = True
    producte = request.session['carro']
    # control per si esborren per GET
    if id_producte in producte:
        del producte[id_producte]
    return HttpResponseRedirect(reverse('comande:veure_comande'))

@login_required
def comfimar_carro(request):
    if 'carro' in request.session:
        comanda=Comanda()
        comanda.usuari=request.user
        comanda.save()
        for clau in request.session['carro']:
            pr = Producte.objects.get(id_producte=clau)
            qtat = request.session['carro'][clau]

            linia=Linia()
            linia.id_comanda=comanda
            linia.id_producte=pr
            linia.quantitat=qtat
            linia.preu = pr.preu
            linia.save()

            pr.stock = pr.stock-qtat
            pr.save()

        del request.session['carro']
    return HttpResponseRedirect(reverse('comande:llista_comandes'))

#veure totes les comandes fetes

@login_required
def llista_comandes(request):
    tipus = Tipus_Producte.objects.all()
    comandes = Comanda.objects.filter(usuari=request.user)
    return render(request, 'comandes/llistaComandes.html', {'comandes':comandes,'tipus': tipus})

@login_required
def detall_comanda(request, id_comanda):
    #productes = get_object_or_404(Linia, pk=id_comanda)
    productes = Linia.objects.filter(id_comanda=id_comanda)
    tipus = Tipus_Producte.objects.all()
    return render(request, 'comandes/detall.html', {'productes': productes, 'tipus': tipus})