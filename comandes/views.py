from django.shortcuts import render, get_object_or_404

from django.http import *
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from productes.models import Tipus_Producte, Producte
from comandes.models import Comanda, Linia
from .forms import compra_producte

#Afagir Producte en el carro
    #de un a un
def update_session(request, id_producte, quantitat=1):
    if 'carro' not in request.session:
        request.session['carro'] ={}
    if id_producte not in request.session['carro']:
        qtat = quantitat
    else:
        qtat = request.session['carro'][id_producte]+1

    request.session['carro'].update({id_producte:qtat})
    messages.add_message(request, messages.SUCCESS, 'El producte ha sigut afegit correctament')
    return HttpResponseRedirect(reverse('producte:veure_productes') )

    #amb la quantitat indicada

def update_sessionPost(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = compra_producte(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if 'carro' not in request.session:
                request.session['carro'] = {}

            request.session['carro'].update({form.cleaned_data['id_producte']: form.cleaned_data['quantitat']})

            messages.add_message(request, messages.SUCCESS, 'El producte ha sigut afegit correctament')
        return HttpResponseRedirect(reverse('producte:veure_productes'))


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
    preu_comanda = 0
    ui_comanda = []
    linies = Linia.objects.filter(id_comanda=id_comanda)
    tipus = Tipus_Producte.objects.all()
    for linia in linies.all():
        pr = Producte.objects.get(id_producte=linia.id_producte_id)
        qtat = linia.quantitat
        preu_total = linia.preu
        preu_comanda += preu_total
        ui_comanda.append({'producte': pr,
                         'quantitat': qtat,
                         'preu_total': preu_total
                         }
                        )

    return render(request, 'comandes/detall.html', {'ui_comanda': ui_comanda, 'preu_comanda': preu_comanda, 'tipus': tipus})