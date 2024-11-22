from django.urls import path
from .views import *

app_name = 'livres'

urlpatterns = [
    path('rechercher/', lister_livres, name='rechercher'),
    path('creer_livre/', creer_livre, name='creer_livre'),
    path('detail_livre/<int:id>/', detail_livre, name='detail_livre'),
    path('creer_auteur/', creer_auteur, name='creer_auteur'),
    path('detail_auteur/<int:id>/', detail_auteur, name='detail_auteur'),
    path('liste_auteurs/', liste_auteurs, name='liste_auteurs'),
    path('modifier_auteur/<int:id>/', modifier_auteur, name='modifier_auteur'),
    path('creer_tag/', creer_tag, name='creer_tag'),
]
