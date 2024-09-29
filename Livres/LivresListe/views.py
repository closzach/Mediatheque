from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *

class SerieViewSet(ModelViewSet):
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer

class AuteurViewSet(ModelViewSet):
    queryset = Auteur.objects.all()
    serializer_class = AuteurSerializer

class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class LecteurViewSet(ModelViewSet):
    queryset = Lecteur.objects.all()
    serializer_class = LecteurSerializer

class LivreViewSet(ModelViewSet):
    queryset = Livre.objects.all()
    serializer_class = LivreSerializer

class LectureViewSet(ModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
