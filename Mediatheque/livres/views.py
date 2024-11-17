from django.shortcuts import render, redirect, get_object_or_404
from .forms import LivreForm, AuteurForm, TagForm
from api.models import Livre, Auteur, Tag

def accueil(request):
    return render(request, 'accueil.html')

def lister_livres(request):
    livres = Livre.objects.all()
    return render(request, 'livres/liste_livres.html', {'livres': livres})

def detail_livre(request, id):
    livre = get_object_or_404(Livre, id=id)
    return render(request, 'livres/detail_livre.html', {'livre', livre})

def creer_livre(request):
    if request.method == 'POST':
        livre_form = LivreForm(request.POST)
        if livre_form.is_valid():
            livre = livre_form.save()
            return redirect('detail_livre', id=livre.id)
    else:
        livre_form = LivreForm()
    return render(request, 'livres/creer_livre.html', {'form': livre_form})

def liste_auteurs(request):
    auteurs = Auteur.objects.all()
    return render(request, 'auteurs/liste_auteurs.html', {'auteurs': auteurs})

def detail_auteur(request, id):
    auteur = get_object_or_404(Auteur, id=id)
    return render(request, 'auteurs/detail_auteur.html', {'auteur': auteur})

def creer_auteur(request):
    if request.method == 'POST':
        auteur_form = AuteurForm(request.POST)
        if auteur_form.is_valid():
            auteur = auteur_form.save()
            return redirect('livres:detail_auteur', id=auteur.id)
    else:
        auteur_form = AuteurForm()
    return render(request, 'auteurs/creer_auteur.html', {'form': auteur_form})

def creer_tag(request):
    if request.method == 'POST':
        tag_form = TagForm(request.POST)
        if tag_form.is_valid():
            tag_form.save()
            return redirect('livres:rechercher')
    else:
        tag_form = TagForm()
    return render(request, 'tags/creer_tag.html', {'form': tag_form})
