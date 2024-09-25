from django.db import models

class Serie(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Auteur(models.Model):
    nom = models.CharField(max_length=100)
    date_naissance = models.DateField(null=True)
    date_mort = models.DateField(null=True)

class Tag(models.Model):
    tag = models.CharField(max_length=100)
    nsfw = models.BooleanField()

class Lecteur(models.Model):
    nom = models.CharField(max_length=100)
    mdp = models.CharField(max_length=255)

class Livre(models.Model):
    nom = models.CharField(max_length=100)
    date_sortie = models.DateField()
    nombre_pages = models.IntegerField()

    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)
    auteurs = models.ManyToManyField(Auteur)
    tags = models.ManyToManyField(Tag)

class Lecture(models.Model):
    date_debut = models.DateField()
    date_fin = models.DateField()
    statut = models.CharField(max_length=20)

    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)
    lecteur = models.ForeignKey(Lecteur, on_delete=models.CASCADE)
