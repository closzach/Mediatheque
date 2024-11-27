from django.db import models
import os
from django.utils.timezone import now
from PIL import Image

class Serie(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Auteur(models.Model):
    nom = models.CharField(max_length=100)
    date_naissance = models.DateField(null=True, blank=True)
    date_mort = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nom

class Tag(models.Model):
    tag = models.CharField(max_length=100)
    nsfw = models.BooleanField()
    modifiable = models.BooleanField(default=True)

    def __str__(self):
        return self.tag

class Lecteur(models.Model):
    nom = models.CharField(max_length=100)
    mdp = models.CharField(max_length=255)
    date_naissance = models.DateField()

    def __str__(self):
        return self.nom
    
def renommer_image(instance, filename):
        extension = os.path.splitext(filename)[1]
        nouveau_nom = f"{instance.id}_{instance.nom}_{now().strftime('%Y%m%d%H%M%S')}{extension}"
        return os.path.join("livres", nouveau_nom)
class Livre(models.Model):
    nom = models.CharField(max_length=100)
    date_sortie = models.DateField()
    nombre_pages = models.IntegerField()
    isbn = models.CharField(max_length=100, unique=True, blank=True, null=True)
    image = models.ImageField(upload_to=renommer_image, default="default.png", blank=True)

    serie = models.ForeignKey(Serie, on_delete=models.CASCADE, null=True, blank=True)
    auteurs = models.ManyToManyField(Auteur)
    tags = models.ManyToManyField(Tag)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            img_path = self.image.path
            with Image.open(img_path) as img:
                max_size = (800, 1200)
                img.thumbnail(max_size)
                img.save(img_path)

    def __str__(self):
        return self.nom

class Lecture(models.Model):
    date_debut = models.DateField(null=True, blank=True)
    date_fin = models.DateField(null=True, blank=True)
    statut = models.CharField(max_length=20)

    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)
    lecteur = models.ForeignKey(Lecteur, on_delete=models.CASCADE)
