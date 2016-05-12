# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.veure_productes, name='veure_productes'),
    url(r'^introduir_producte/$', views.intro_edit_producte, name='introduir_producte'),
    url(r'^editar_producte/(?P<id_producte>[0-9]+)/$', views.intro_edit_producte, name='editar_producte'),
    url(r'^eliminar_producte/(?P<id_producte>[0-9]+)/$', views.eliminar_producte, name='eliminar_producte'),
    url(r'^veure_detall/(?P<id_producte>[0-9]+)/$', views.veure_detall, name='veure_detall'),
    url(r'^filtrar_tipus/(?P<id_tipus>[0-9]+)/$', views.filtrar_tipus, name='filtrar_tipus'),
    url(r'^filtrar_marcas/(?P<id_marca>[0-9]+)/$', views.filtrar_marcas, name='filtrar_marcas'),

    url(r'^tipus/$', views.veure_tipus, name='veure_tipus'),
    url(r'^tipus/introduir_tipus/$', views.intro_edit_tipus, name='introduir_tipus'),
    url(r'^tipus/editar_tipus/(?P<id_tipus>[0-9]+)/$', views.intro_edit_tipus, name='editar_tipus'),
    url(r'^tipus/eliminar_tipus/(?P<id_tipus>[0-9]+)/$', views.eliminar_tipus, name='eliminar_tipus'),

    url(r'^marcas/$', views.veure_marcas, name='veure_marcas'),
    url(r'^marcas/introduir_marca/$', views.intro_edit_marca, name='introduir_marca'),
    url(r'^marcas/editar_marca/(?P<id_marca>[0-9]+)/$', views.intro_edit_marca, name='editar_marca'),
    url(r'^marcas/eliminar_marca/(?P<id_marca>[0-9]+)/$', views.eliminar_marca, name='eliminar_marca'),
]