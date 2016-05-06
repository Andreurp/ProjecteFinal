from __future__ import unicode_literals

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.veure_productes, name='veure_productes'),
    url(r'^introduir_producte/$', views.intro_edit_producte, name='introduir_producte'),
]