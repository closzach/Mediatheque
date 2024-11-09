from django.urls import path, include
from .views import *

app_name = 'livres'

urlpatterns = [
    path('accueil', accueil, name='accueil')
]
