# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.core.urlresolvers import reverse
from django.forms import modelform_factory
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from productes.models import Producte, Tipus_Producte, Marca_Producte

# Create your views here.
# pruductes

def veure_productes(request):
    productes = Producte.objects.all()
    tipus = Tipus_Producte.objects.all()
    return render(request, 'productes/index.html', {'productes': productes, 'tipus': tipus})

@login_required
def intro_edit_producte(request, id_producte=None):
    tipus = Tipus_Producte.objects.all()
    es_modificacio =(id_producte!=None)
    producteForm =modelform_factory(Producte, exclude=())
    if es_modificacio:
        producte = get_object_or_404(Producte, id_producte=id_producte)
    else:
        producte=Producte()
    if request.method == 'POST':
        form = producteForm(request.POST,request.FILES,instance=producte)
        if form.is_valid():
            producte = form.save()
            if(es_modificacio):
                messages.add_message(request, messages.SUCCESS, 'El producte ha sigut modificat correctament')
            else:
                messages.add_message(request, messages.SUCCESS, 'El nou producte ha sigut creat correctament')
            return HttpResponseRedirect(reverse('producte:veure_productes'))
        else:
            if(es_modificacio):
                messages.add_message(request, messages.ERROR, 'Error en modificar el producte')
            else:
                messages.add_message(request, messages.ERROR, 'Error en crear el producte nova')
    else:
        form = producteForm(instance=producte)

    form.helper = FormHelper()
    form.helper.form_class = 'form-horizontal col-md-8 col-md-offset-2'
    form.helper.label_class = 'col-lg-3'
    form.helper.field_class = 'col-lg-9'
    form.helper.add_input(Submit('submit', 'Enviar'))
    return render(request, 'formulari.html', {'form': form, 'producte':producte, 'tipus': tipus})

@login_required
def eliminar_producte(request, id_producte):
    producte = get_object_or_404(Producte, pk=id_producte)
    messages.add_message(request, messages.SUCCESS,'El producta ha sigut eliminada correctament')
    producte.delete()
    return HttpResponseRedirect(reverse('producte:veure_productes') )

#Tipus_admin

@login_required
def veure_tipus(request):
    tipus = Tipus_Producte.objects.all()
    return render(request, 'tipus/index.html', {'tipus': tipus})


#Marcas_admin

@login_required
def veure_marcas(request):
    marcas = Marca_Producte.objects.all()
    return render(request, 'marcas/index.html', {'marcas': marcas})

#carreo compre

def update_session(request, id_producte):
    #if not request.is_ajax() or not request.method=='POST':
     #   return HttpResponseNotAllowed(['POST'])

    if 'carro' not in request.session:
        request.session['carro'] =[id_producte,1]
    else:
        request.session['carro'] += [id_producte,1]

    messages.add_message(request, messages.SUCCESS, 'El producte ha sigut afegit correctament')
    return HttpResponseRedirect(reverse('producte:veure_productes') )