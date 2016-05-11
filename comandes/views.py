from django.shortcuts import render

# Create your views here.
from django.http import *
from django.contrib import messages
from django.core.urlresolvers import reverse

#Afagir Producte

def update_session(request, id_producte):
    if 'carro' not in request.session:
        request.session['carro'] =[id_producte,1]
    else:
        request.session['carro'] += [id_producte,1]

    messages.add_message(request, messages.SUCCESS, 'El producte ha sigut afegit correctament')
    return HttpResponseRedirect(reverse('producte:veure_productes') )

def veure_comande(request):
    #comandes = Comanda.objects.all()
    comandes =(request.session['carro'])
    return render(request, 'comandes/index.html', {'comande': comandes})