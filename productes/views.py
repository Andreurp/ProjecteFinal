# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.http import HttpResponseRedirect
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.core.urlresolvers import reverse
from django.forms import modelform_factory
from django.contrib import messages

from productes.models import Producte, Tipus_Producte

# Create your views here.
# pruductes

def veure_productes(request):
    productes = Producte.objects.all()
    return render(request, 'productes/index.html', {'productes': productes, 'h1':"Productes"})

def intro_edit_producte(request, id_producte=None):
    es_modificacio =(id_producte!=None)
    producteForm =modelform_factory(Producte, exclude=())
    if es_modificacio:
        producte = get_object_or_404(Producte, id=id_producte)
    else:
        producte=Producte()
    if request.method == 'POST':
        form = producteForm(request.POST,request.FILES,instance=producte)
        if form.is_valid():
            producte = form.save()
            if(es_modificacio):
                messages.add_message(request, messages.SUCCESS, 'El producta ha sigut modificat correctament')
            else:
                messages.add_message(request, messages.SUCCESS, 'El nou producta ha sigut creada ')
            return HttpResponseRedirect(reverse('producte:veure_productes'))
        else:
            if(es_modificacio):
                messages.add_message(request, messages.ERROR, 'Error en modificar la carta')
            else:
                messages.add_message(request, messages.ERROR, 'Error en crear la carta nova')
    else:
        form = producteForm(instance=producte)

    form.helper = FormHelper()
    form.helper.form_class = 'form-horizontal col-md-8 col-md-offset-2'
    form.helper.label_class = 'col-lg-2'
    form.helper.field_class = 'col-lg-10'
    form.helper.add_input(Submit('submit', 'Enviar'))
    return render(request, 'formulari.html', {'form': form, 'producte':producte, 'h1':"Edita el producta"})

def eliminar_producte(request, id_producte):
    producte = get_object_or_404(Producte, pk=id_producte)
    messages.add_message(request, messages.SUCCESS,'El producta ha sigut eliminada correctament')
    producte.delete()
    return HttpResponseRedirect(reverse('producte:veure_productes') )

#Tipus

def veure_tipus(request):
    tipus = Tipus_Producte.objects.all()
    return render(request, 'productes/index.html', {'productes': tipus})
