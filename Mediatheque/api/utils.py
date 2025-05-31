from django.utils import timezone
from datetime import timedelta

def est_majeur(user):
    today = timezone.now().date()
    age = today - user.date_naissance
    majorite = timedelta(days=365*18)
    return age>=majorite

def livre_pour_adulte(livre):
    len(livre.tags.filter(pour_adulte=True))>0
