# encoding: utf-8
from django.contrib import admin

from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from usuaris import views as vista_usuaris

urlpatterns = ([
    url(r'^admin/', admin.site.urls),
    url(r'^', include('productes.urls', namespace='producte')),

    url(r'^login/', vista_usuaris.vista_login, name="login"),
    url(r'^registrar/', vista_usuaris.registrar, name="registrar"),
    url(r'^sortir/', vista_usuaris.logout_view, name="sortir"),
]

    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    )
