# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.veure_productes, name='veure_productes'),
    url(r'^introduir_producte/$', views.intro_edit_producte, name='introduir_producte'),
    url(r'^editar_producte/(?P<id_producte>[0-9]+)/$', views.intro_edit_producte, name='editar_producte'),
    url(r'^eliminar_producte/(?P<id_producte>[0-9]+)/$', views.eliminar_producte, name='eliminar_producte'),

    url(r'^tipus/$', views.veure_tipus, name='veure_tipus'),

    url(r'^marcas/$', views.veure_marcas, name='veure_marcas'),
]