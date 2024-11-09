from django.contrib import admin
from api.models import *

admin.site.register([
    Serie,
    Auteur,
    Tag,
    Lecteur,
    Livre,
    Lecture
])
