from django.urls import path, include
from .views import *

urlpatterns = [
    path('accueil', accueil, name='accueil')
]
