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
# Productes

def veure_productes(request):
    productes = Producte.objects.all()
    tipus = Tipus_Producte.objects.all()
    marcas = Marca_Producte.objects.all()
    return render(request, 'productes/index.html', {'productes': productes, 'tipus': tipus, 'marcas': marcas})

@login_required
def intro_edit_producte(request, id_producte=None):
    if (request.user.username != "admin"):
        messages.add_message(request, messages.ERROR, 'No tens permisos per fer aquesta acció')
        return HttpResponseRedirect(reverse('producte:veure_productes'))
    else:
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
                    messages.add_message(request, messages.ERROR, 'Error en crear el producte nou')
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
    if (request.user.username != "admin"):
        messages.add_message(request, messages.ERROR, 'No tens permisos per fer aquesta acció')
    else:
        producte = get_object_or_404(Producte, pk=id_producte)
        messages.add_message(request, messages.SUCCESS,'El producta ha sigut eliminat correctament')
        producte.delete()
    return HttpResponseRedirect(reverse('producte:veure_productes') )

def veure_detall(request, id_producte):
    producte = get_object_or_404(Producte, pk=id_producte)
    estoc = range(1,producte.stock+1)
    tipus = Tipus_Producte.objects.all()
    marcas = Marca_Producte.objects.all()
    return render(request, 'productes/detall.html', {'producte': producte, 'tipus': tipus, 'marcas': marcas, 'estoc': estoc})

#Tipus

@login_required
def veure_tipus(request):
    if (request.user.username != "admin"):
        messages.add_message(request, messages.ERROR, 'No tens permisos per fer aquesta acció')
        return HttpResponseRedirect(reverse('producte:veure_productes'))
    else:
        tipus = Tipus_Producte.objects.all()
        return render(request, 'tipus/index.html', {'tipus': tipus})

@login_required
def intro_edit_tipus(request, id_tipus=None):
    if (request.user.username != "admin"):
        messages.add_message(request, messages.ERROR, 'No tens permisos per fer aquesta acció')
        return HttpResponseRedirect(reverse('producte:veure_productes'))
    else:
        es_modificacio =(id_tipus!=None)
        tipusForm =modelform_factory(Tipus_Producte, exclude=())
        if es_modificacio:
            tipus = get_object_or_404(Tipus_Producte, id=id_tipus)
        else:
            tipus=Tipus_Producte()
        if request.method == 'POST':
            form = tipusForm(request.POST,instance=tipus)
            if form.is_valid():
                tipus = form.save()
                if(es_modificacio):
                    messages.add_message(request, messages.SUCCESS, 'El tipu ha sigut modificat correctament')
                else:
                    messages.add_message(request, messages.SUCCESS, 'El nou tipu ha sigut creat correctament')
                return HttpResponseRedirect(reverse('producte:veure_tipus'))
            else:
                if(es_modificacio):
                    messages.add_message(request, messages.ERROR, 'Error en modificar el tipu')
                else:
                    messages.add_message(request, messages.ERROR, 'Error en crear el tipu nou')
        else:
            form = tipusForm(instance=tipus)

        form.helper = FormHelper()
        form.helper.form_class = 'form-horizontal col-md-8 col-md-offset-2'
        form.helper.label_class = 'col-lg-3'
        form.helper.field_class = 'col-lg-9'
        form.helper.add_input(Submit('submit', 'Enviar'))
        return render(request, 'formulari.html', {'form': form, 'tipu': tipus})

@login_required
def eliminar_tipus(request, id_tipus):
    if (request.user.username != "admin"):
        messages.add_message(request, messages.ERROR, 'No tens permisos per fer aquesta acció')
        return HttpResponseRedirect(reverse('producte:veure_productes'))
    else:
        tipu = get_object_or_404(Tipus_Producte, pk=id_tipus)
        messages.add_message(request, messages.SUCCESS,'El tipu ha sigut eliminat correctament')
        tipu.delete()
        return HttpResponseRedirect(reverse('producte:veure_tipus') )

def filtrar_tipus(request, id_tipus):
    productes = Producte.objects.filter(tipus_id=id_tipus)
    tipus = Tipus_Producte.objects.all()
    marcas = Marca_Producte.objects.all()
    return render(request, 'productes/index.html', {'productes': productes, 'tipus': tipus, 'marcas': marcas})

#Marques

@login_required
def veure_marcas(request):
    if (request.user.username != "admin"):
        messages.add_message(request, messages.ERROR, 'No tens permisos per fer aquesta acció')
        return HttpResponseRedirect(reverse('producte:veure_productes'))
    else:
        tipus = Tipus_Producte.objects.all()
        marcas = Marca_Producte.objects.all()
        return render(request, 'marcas/index.html', {'marcas': marcas, 'tipus': tipus})

@login_required
def intro_edit_marca(request, id_marca=None):
    if (request.user.username != "admin"):
        messages.add_message(request, messages.ERROR, 'No tens permisos per fer aquesta acció')
        return HttpResponseRedirect(reverse('producte:veure_productes'))
    else:
        es_modificacio =(id_marca!=None)
        marcaForm =modelform_factory(Marca_Producte, exclude=())
        if es_modificacio:
            marca = get_object_or_404(Marca_Producte, id=id_marca)
        else:
            marca=Marca_Producte()
        if request.method == 'POST':
            form = marcaForm(request.POST,instance=marca)
            if form.is_valid():
                marca = form.save()
                if(es_modificacio):
                    messages.add_message(request, messages.SUCCESS, 'La marca ha sigut modificada correctament')
                else:
                    messages.add_message(request, messages.SUCCESS, 'La nova marca ha sigut creada correctament')
                return HttpResponseRedirect(reverse('producte:veure_marcas'))
            else:
                if(es_modificacio):
                    messages.add_message(request, messages.ERROR, 'Error en modificar la marca')
                else:
                    messages.add_message(request, messages.ERROR, 'Error en crear la marca nova')
        else:
            form = marcaForm(instance=marca)

        form.helper = FormHelper()
        form.helper.form_class = 'form-horizontal col-md-8 col-md-offset-2'
        form.helper.label_class = 'col-lg-3'
        form.helper.field_class = 'col-lg-9'
        form.helper.add_input(Submit('submit', 'Enviar'))
        return render(request, 'formulari.html', {'form': form, 'marca': marca})

@login_required
def eliminar_marca(request, id_marca):
    if (request.user.username != "admin"):
        messages.add_message(request, messages.ERROR, 'No tens permisos per fer aquesta acció')
        return HttpResponseRedirect(reverse('producte:veure_productes'))
    else:
        marca = get_object_or_404(Marca_Producte, pk=id_marca)
        messages.add_message(request, messages.SUCCESS,'La marca ha sigut eliminada correctament')
        marca.delete()
        return HttpResponseRedirect(reverse('producte:veure_marcas') )

def filtrar_marcas(request, id_marca):
    productes = Producte.objects.filter(marca_id=id_marca)
    tipus = Tipus_Producte.objects.all()
    marcas = Marca_Producte.objects.all()
    return render(request, 'productes/index.html', {'productes': productes, 'tipus': tipus, 'marcas': marcas})