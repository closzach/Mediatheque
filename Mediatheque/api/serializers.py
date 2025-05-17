from rest_framework.serializers import ModelSerializer
from .models import *

class AuteurSerializer(ModelSerializer):
    class Meta:
        model = Auteur
        fields = '__all__'

class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class LivreSerializer(ModelSerializer):
    auteurs = AuteurSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Livre
        fields = '__all__'

class LectureSerializer(ModelSerializer):
    livre = LivreSerializer(read_only=True)
    lecteur = UserSerializer(read_only=True)

    class Meta:
        model = Lecture
        fields = '__all__'
