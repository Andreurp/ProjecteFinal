# encoding: utf-8
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.http import HttpResponseRedirect
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.core.urlresolvers import reverse
from django.forms import modelform_factory
from django.contrib import messages

from productes.models import Producte

# Create your views here.
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
                messages.add_message(request, messages.SUCCESS, 'La seva carta ha sigut modificat correctament')
            else:
                messages.add_message(request, messages.SUCCESS, 'la nova carta ha sigut creada ')
            return HttpResponseRedirect(reverse('producte:veure_productes'))
        else:
            if(es_modificacio):
                messages.add_message(request, messages.ERROR, 'Error en modificar la carta')
            else:
                messages.add_message(request, messages.ERROR, 'Error en crear la carta nova')
    else:
        form = producteForm(instance=producte)

    form.helper = FormHelper()
    form.helper.form_class = 'form-horizontal'
    form.helper.label_class = 'col-md-6 col-md-offset-3'
    form.helper.field_class = 'col-md-9'
    form.helper.add_input(Submit('submit', 'Enviar'))
    return render(request, 'formulari.html', {'form': form, 'producte':producte, 'h1':"Edita la teva carta"})