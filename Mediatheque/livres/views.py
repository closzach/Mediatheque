from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.core.exceptions import PermissionDenied
from .forms import LivreForm, AuteurForm, TagForm, SearchForm
from api.models import Livre, Auteur, Tag

def lister_livres(request):
    livres = Livre.objects.prefetch_related('auteurs')
    tags = Tag.objects.all()
    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            recherche = search_form.cleaned_data['recherche']
            if recherche == "":
                livres = Livre.objects.all()
            else:
                livres = Livre.objects.filter(nom__icontains=recherche).prefetch_related('auteurs')
    else:
        search_form = SearchForm()
    return render(request, 'livres/liste_livres.html', {'livres': livres, 'tags': tags, 'search_form': search_form})

def detail_livre(request, id):
    livre = get_object_or_404(Livre, id=id)
    auteurs = Auteur.objects.filter(livre=livre)
    tags = Tag.objects.filter(livre=livre)
    return render(request, 'livres/detail_livre.html', {'livre': livre, 'auteurs': auteurs, 'tags': tags})

def creer_livre(request):
    if request.method == 'POST':
        livre_form = LivreForm(request.POST, request.FILES)
        if livre_form.is_valid():
            livre = livre_form.save()
            return redirect('livres:detail_livre', id=livre.id)
    else:
        livre_form = LivreForm()
    return render(request, 'livres/creer_livre.html', {'form': livre_form})

def modifier_livre(request, id):
    livre = get_object_or_404(Livre, id=id)
    livre_form = LivreForm(instance=livre)
    if request.method == 'POST':
        livre_form = LivreForm(request.POST, instance=livre)
        if livre_form.has_changed() and livre_form.is_valid():
            livre_form.save()
            return redirect('livres:detail_livre', id=id)
    return render(request, 'livres/modifier_livre.html', {'livre': livre, 'form': livre_form})

def supprimer_livre(request, id):
    if request.method == "POST":
        livre = get_object_or_404(Livre, id=id)
        livre.delete()
        return redirect('livres:rechercher')
    return redirect(reverse('livres:detail_livre', args=[id]))

def liste_auteurs(request):
    auteurs = Auteur.objects.all()
    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            recherche = search_form.cleaned_data['recherche']
            if recherche == "":
                auteurs = Auteur.objects.all()
            else:
                auteurs = Auteur.objects.filter(nom__icontains=recherche)
    else:
        search_form = SearchForm()
    return render(request, 'auteurs/liste_auteurs.html', {'auteurs': auteurs, 'search_form': search_form})

def detail_auteur(request, id):
    auteur = get_object_or_404(Auteur, id=id)
    livres = Livre.objects.filter(auteurs=auteur)
    return render(request, 'auteurs/detail_auteur.html', {'auteur': auteur, 'livres': livres})

def creer_auteur(request):
    if request.method == 'POST':
        auteur_form = AuteurForm(request.POST)
        if auteur_form.is_valid():
            auteur = auteur_form.save()
            return redirect('livres:detail_auteur', id=auteur.id)
    else:
        auteur_form = AuteurForm()
    return render(request, 'auteurs/creer_auteur.html', {'form': auteur_form})

def modifier_auteur(request, id):
    auteur = get_object_or_404(Auteur, id=id)
    auteur_form = AuteurForm(instance=auteur)
    if request.method == 'POST':
        auteur_form = AuteurForm(request.POST, instance=auteur)
        if auteur_form.has_changed() and auteur_form.is_valid():
            auteur_form.save()
            return redirect('livres:detail_auteur', id=id)
    return render(request, 'auteurs/modifier_auteur.html', {'auteur': auteur, 'form': auteur_form})

def supprimer_auteur(request, id):
    if request.method == "POST":
        auteur = get_object_or_404(Auteur, id=id)
        auteur.delete()
        return redirect('livres:liste_auteurs')
    return redirect(reverse('livres:detail_auteur', args=[id]))

def creer_tag(request):
    if request.method == 'POST':
        tag_form = TagForm(request.POST)
        if tag_form.is_valid():
            tag_form.save()
            return redirect('livres:liste_tags')
    else:
        tag_form = TagForm()
    return render(request, 'tags/creer_tag.html', {'form': tag_form})

def lister_tags(request):
    tags = Tag.objects.all()
    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            recherche = search_form.cleaned_data['recherche']
            if recherche == "":
                tags = Tag.objects.all()
            else:
                tags = Tag.objects.filter(tag__icontains=recherche)
    else:
        search_form = SearchForm()
    return render(request, 'tags/liste_tags.html', {'tags': tags, 'search_form': search_form})

def modifier_tag(request, id):
    tag = get_object_or_404(Tag, id=id)
    tag_form = TagForm(instance=tag)
    if request.method == 'POST':
        if not tag.modifiable:
            raise PermissionDenied("Ce tag ne peut être modifié.")
        tag_form = TagForm(request.POST, instance=tag)
        if tag_form.has_changed() and tag_form.is_valid():
            tag_form.save()
            return redirect('livres:liste_tags')
    return render(request, 'auteurs/modifier_auteur.html', {'tag': tag, 'form': tag_form})

def supprimer_tag(request, id):
    if request.method == "POST":
        tag = get_object_or_404(Tag, id=id)
        if not tag.modifiable:
            raise PermissionDenied("Ce tag ne peut être supprimé.")
        tag.delete()
    return redirect('livres:liste_tags')
