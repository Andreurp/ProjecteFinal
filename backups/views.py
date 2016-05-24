from django.core.urlresolvers import reverse
from django.http import *
from django.core.management import call_command
import datetime
import sys

def mostra_backups(request):

    return True

def fer_backups(request):
    sysout = sys.stdout
    nomFitxer = "backups/media/bdd-Backup" + str(datetime.datetime.now()).replace(" ","").replace(":","-")+".xml"
    sys.stdout = open (nomFitxer, 'w')
    call_command('dumpdata',indent=2,format='xml')
    sys.stdout = sysout
    return HttpResponseRedirect(reverse('producte:veure_productes'))

