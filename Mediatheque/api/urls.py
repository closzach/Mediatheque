from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('auteurs', AuteurViewSet)
router.register('tags', TagViewSet)
router.register('lecteurs', LecteurViewSet)
router.register('livres', LivreViewSet)
router.register('lectures', LectureViewSet)

urlpatterns = [
    path('', include(router.urls))
]