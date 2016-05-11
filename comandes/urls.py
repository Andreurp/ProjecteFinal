# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^veure_comande/$', views.veure_comande, name='veure_comande'),

    url(r'^update_session/(?P<id_producte>[0-9]+)/$', views.update_session, name='update_session'),
]