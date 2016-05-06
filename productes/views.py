from django.shortcuts import render
from productes.models import Producte

# Create your views here.
def veure_productes(request):
    productes = Producte.objects.all()
    return render(request, 'productes/index.html', {'productes': productes, 'h1':"Productes"})