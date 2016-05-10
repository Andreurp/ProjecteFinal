# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^veure_comande/$', views.veure_comande, name='veure_comande'),
]