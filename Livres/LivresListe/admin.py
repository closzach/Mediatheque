from django.contrib import admin
from LivresListe.models import *

admin.site.register([
    Serie,
    Auteur,
    Tag,
    Lecteur,
    Livre,
    Lecture
])
