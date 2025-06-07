from django.urls import path
from .views import *

app_name = 'livres'

urlpatterns = [
    path('rechercher/', lister_livres, name='rechercher'),
    path('livre/creer/', creer_livre, name='creer_livre'),
    path('livre/<int:id>/', detail_livre, name='detail_livre'),
    path('livre/<int:id>/modifier/', modifier_livre, name='modifier_livre'),
    path('livre/<int:id>/supprimer/', supprimer_livre, name='supprimer_livre'),
    path('auteur/creer/', creer_auteur, name='creer_auteur'),
    path('auteur/<int:id>/', detail_auteur, name='detail_auteur'),
    path('auteurs/', liste_auteurs, name='liste_auteurs'),
    path('auteur/<int:id>/modifier/', modifier_auteur, name='modifier_auteur'),
    path('auteur/<int:id>/supprimer/', supprimer_auteur, name='supprimer_auteur'),
    path('tag/creer/', creer_tag, name='creer_tag'),
    path('tags/', lister_tags, name='liste_tags'),
    path('tag/<int:id>/modifier/', modifier_tag, name='modifier_tag'),
    path('tag/<int:id>/supprimer/', supprimer_tag, name='supprimer_tag'),
    path('bibliotheque/', bibliotheque, name='bibliotheque'),
    path('livre/<int:id>/ajouter/', ajouter_livre, name='ajouter_livre'),
    path('lecture/<int:id>/supprimer/', supprimer_lecture, name='supprimer_lecture'),
    path('lecture/<int:id>/', detail_lecture, name='detail_lecture'),
    path('lecture/<int:id>/modifier/', modifier_lecture, name='modifier_lecture'),
    path('lecture/<int:id>/modifier_mp/', modifier_marque_pages, name='modifier_marque_pages'),
    path('wishlist/<int:id>/ajouter/', ajouter_souhait, name="ajouter_souhait"),
    path('wishlist/<int:id>/retirer/', retirer_souhait, name="retirer_souhait"),
    path('wishlist/', liste_de_souhaits, name='liste_de_souhaits'),
]
