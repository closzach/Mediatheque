from django.urls import path
from .views import *

app_name = 'livres'

urlpatterns = [
    path('rechercher/', lister_livres, name='rechercher'),
    path('livre/creer/', creer_livre, name='creer_livre'),
    path('livre/<int:id>/', detail_livre, name='detail_livre'),
    path('livre/modifier/<int:id>/', modifier_livre, name='modifier_livre'),
    path('livre/supprimer/<int:id>/', supprimer_livre, name='supprimer_livre'),
    path('auteur/creer/', creer_auteur, name='creer_auteur'),
    path('auteur/<int:id>/', detail_auteur, name='detail_auteur'),
    path('auteurs/', liste_auteurs, name='liste_auteurs'),
    path('auteur/modifier/<int:id>/', modifier_auteur, name='modifier_auteur'),
    path('auteur/supprimer/<int:id>/', supprimer_auteur, name='supprimer_auteur'),
    path('tag/creer/', creer_tag, name='creer_tag'),
    path('tags/', lister_tags, name='liste_tags'),
    path('tag/modifier/<int:id>', modifier_tag, name='modifier_tag'),
    path('tag/supprimer/<int:id>', supprimer_tag, name='supprimer_tag'),
    path('bibliotheque/', bibliotheque, name='bibliotheque'),
    path('livre/ajouter/<int:id>', ajouter_livre, name='ajouter_livre'),
    path('lecture/supprimer/<int:id>', supprimer_lecture, name='supprimer_lecture'),
    path('lecture/<int:id>', detail_lecture, name='detail_lecture'),
    path('lecture/modifier/<int:id>', modifier_lecture, name='modifier_lecture'),
    path('lecture/modifier_mp/<int:id>', modifier_marque_pages, name='modifier_marque_pages'),
]
