from django.contrib import admin
from api.models import *

admin.site.register([
    Auteur,
    Tag,
    Lecteur,
    Livre,
    Lecture
])
