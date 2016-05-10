from django.shortcuts import render

# Create your views here.
from comandes.models import Comanda

def veure_comande(request):
    #comandes = Comanda.objects.all()
    comandes =(request.session['carro'])
    return render(request, 'comandes/index.html', {'comande': comandes})