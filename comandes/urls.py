# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^update_session/(?P<id_producte>[0-9]+)/$', views.update_session, name='update_session'),

    url(r'^veure_comande/$', views.veure_comande, name='veure_comande'),
    url(r'^veure_comande/esborra_carro/$', views.esborra_carro, name='esborra_carro'),
    url(r'^veure_comande/esborra_linia/(?P<id_producte>[0-9]+)/$', views.esborra_linia, name='esborra_linia'),
]