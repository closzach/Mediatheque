from django.utils import timezone
from datetime import timedelta

def est_majeur(lecteur):
    today = timezone.now().date()
    age = today - lecteur.date_naissance
    majorite = timedelta(days=365*18)
    return age>=majorite

def livre_pour_adulte(livre):
    len(livre.tags.filter(pour_adulte=True))>0
