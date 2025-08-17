from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.core.exceptions import PermissionDenied
from .forms import LivreForm, AuteurForm, TagForm, SearchForm, SearchLivreForm, SearchLectureForm, LectureForm, MarquePagesForm
from api.models import Livre, Auteur, Tag, Lecture
from django.contrib.auth.decorators import login_required, permission_required
from api.utils import est_majeur
from django.contrib import messages
from django.db.models import Avg

def lister_livres(request):
    if request.user.is_authenticated and est_majeur(request.user) and not request.user.cacher_pour_adulte:
        livres = Livre.objects.prefetch_related('auteurs')
    else:
        livres = Livre.objects.exclude(tags__pour_adulte=True).prefetch_related('auteurs')
    if request.method == 'POST':
        search_form = SearchLivreForm(request.POST)
        if search_form.is_valid():
            recherche = search_form.cleaned_data['recherche']
            tags_recherche = search_form.cleaned_data['tags']
            auteur_recherche = search_form.cleaned_data['auteur']
            if recherche == "":
                if request.user.is_authenticated and est_majeur(request.user) and not request.user.cacher_pour_adulte:
                    livres = Livre.objects.prefetch_related('auteurs')
                else:
                    livres = Livre.objects.exclude(tags__pour_adulte=True).prefetch_related('auteurs')
            else:
                if request.user.is_authenticated and est_majeur(request.user) and not request.user.cacher_pour_adulte:
                    livres = Livre.objects.filter(nom__icontains=recherche).prefetch_related('auteurs')
                else:
                    livres = Livre.objects.exclude(tags__pour_adulte=True).filter(nom__icontains=recherche).prefetch_related('auteurs')
            if len(tags_recherche)>0:
                for tag_recherche in tags_recherche:
                    if request.user.is_authenticated and est_majeur(request.user) and not request.user.cacher_pour_adulte:
                        livres = Livre.objects.filter(tags__id=tag_recherche.id).distinct().prefetch_related('auteurs')
                    else:
                        livres = Livre.objects.exclude(tags__pour_adulte=True).filter(tags__id=tag_recherche.id).distinct().prefetch_related('auteurs')
            if auteur_recherche:
                if request.user.is_authenticated and est_majeur(request.user) and not request.user.cacher_pour_adulte:
                    livres = Livre.objects.filter(auteurs__id=auteur_recherche.id).prefetch_related('auteurs')
                else:
                    livres = Livre.objects.exclude(tags__pour_adulte=True).filter(auteurs__id=auteur_recherche.id).prefetch_related('auteurs')
    else:
        search_form = SearchLivreForm()
    return render(request, 'livres/liste_livres.html', {'livres': livres, 'search_form': search_form})

def detail_livre(request, id):
    livre = get_object_or_404(Livre, id=id)
    if len(livre.tags.filter(pour_adulte=True))>0 and (not request.user.is_authenticated or not est_majeur(request.user) or request.user.cacher_pour_adulte):
        raise PermissionDenied("Vous ne pouvez pas voir ce contenu.")
    auteurs = livre.auteurs.all()
    tags = livre.tags.all()
    bouton_ajouter = True
    lecture = None
    souhait = False

    if request.user.is_authenticated:
        if len(Lecture.objects.filter(lecteur=request.user, livre=livre))!=0:
            lecture = Lecture.objects.filter(lecteur=request.user, livre=livre).first()
            bouton_ajouter = False
        if livre in Livre.objects.filter(user=request.user):
            souhait = True

    moyenne = Lecture.objects.filter(livre=livre, note__isnull=False).aggregate(moyenne=Avg('note'))['moyenne']
    if moyenne:
        moyenne = round(moyenne, 1)

    return render(request, 'livres/detail_livre.html', {'livre': livre, 'auteurs': auteurs, 'tags': tags, 'bouton_ajouter': bouton_ajouter, 'lecture': lecture, 'souhait': souhait, 'moyenne': moyenne})

@permission_required('api.creer_livre')
def creer_livre(request):
    if request.method == 'POST':
        livre_form = LivreForm(request.POST, request.FILES)
        if livre_form.is_valid():
            livre = livre_form.save()
            return redirect('livres:detail_livre', id=livre.id)
    else:
        livre_form = LivreForm()
    return render(request, 'livres/creer_livre.html', {'form': livre_form})

@permission_required('api.modifier_livre')
def modifier_livre(request, id):
    livre = get_object_or_404(Livre, id=id)
    if len(livre.tags.filter(pour_adulte=True))>0 and (not request.user.is_authenticated or not est_majeur(request.user) or request.user.cacher_pour_adulte):
        raise PermissionDenied("Vous ne pouvez pas voir ce contenu.")
    livre_form = LivreForm(instance=livre)
    if request.method == 'POST':
        livre_form = LivreForm(request.POST, request.FILES, instance=livre)
        if livre_form.has_changed() and livre_form.is_valid():
            livre_form.save()
            return redirect('livres:detail_livre', id=id)
    return render(request, 'livres/modifier_livre.html', {'livre': livre, 'form': livre_form})

@permission_required('api.supprimer_livre')
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
    if request.user.is_authenticated and est_majeur(request.user) and not request.user.cacher_pour_adulte:
        livres = Livre.objects.filter(auteurs__id=auteur.id)
    else:
        livres = Livre.objects.exclude(tags__pour_adulte=True).filter(auteurs__id=auteur.id)
    return render(request, 'auteurs/detail_auteur.html', {'auteur': auteur, 'livres': livres})

@permission_required('api.creer_auteur')
def creer_auteur(request):
    if request.method == 'POST':
        auteur_form = AuteurForm(request.POST)
        if auteur_form.is_valid():
            auteur = auteur_form.save()
            return redirect('livres:detail_auteur', id=auteur.id)
    else:
        auteur_form = AuteurForm()
    return render(request, 'auteurs/creer_auteur.html', {'form': auteur_form})

@permission_required('api.modifier_auteur')
def modifier_auteur(request, id):
    auteur = get_object_or_404(Auteur, id=id)
    auteur_form = AuteurForm(instance=auteur)
    if request.method == 'POST':
        auteur_form = AuteurForm(request.POST, instance=auteur)
        if auteur_form.has_changed() and auteur_form.is_valid():
            auteur_form.save()
            return redirect('livres:detail_auteur', id=id)
    return render(request, 'auteurs/modifier_auteur.html', {'auteur': auteur, 'form': auteur_form})

@permission_required('api.supprimer_livre')
def supprimer_auteur(request, id):
    if request.method == "POST":
        auteur = get_object_or_404(Auteur, id=id)
        auteur.delete()
        return redirect('livres:liste_auteurs')
    return redirect(reverse('livres:detail_auteur', args=[id]))

@permission_required('api.creer_tag')
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

@permission_required('api.modifier_tag')
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
    return render(request, 'tags/modifier_tag.html', {'tag': tag, 'form': tag_form})

@permission_required('api.supprimer_tag')
def supprimer_tag(request, id):
    tag = get_object_or_404(Tag, id=id)

    if not tag.modifiable:
        raise PermissionDenied("Ce tag ne peut être supprimé.")

    tag.delete()
    return redirect('livres:liste_tags')

@login_required
def bibliotheque(request):
    lectures = Lecture.objects.filter(lecteur=request.user)
    if request.method == 'POST':
        search_form = SearchLectureForm(request.POST)
        if search_form.is_valid():
            recherche = search_form.cleaned_data['recherche']
            statut = search_form.cleaned_data['statut']
            if recherche != "":
                lectures = lectures.filter(livre__nom__icontains=recherche)
            if statut != "":
                lectures = lectures.filter(statut=statut)
    else:
        search_form = SearchLectureForm()
    lectures_a_lire = lectures.filter(statut='a lire')
    lectures_lues = lectures.filter(statut='lu')
    lectures_en_cours = lectures.filter(statut='en cours')
    lectures_abandonnees = lectures.filter(statut='abandonne')
    lectures_en_pause = lectures.filter(statut='en pause')
    return render(request, 'lectures/bibliotheque.html', {'lectures': lectures, 'lectures_a_lire': lectures_a_lire, 'lectures_lues': lectures_lues, 'lectures_en_cours': lectures_en_cours, 'lectures_abandonnees': lectures_abandonnees, 'lectures_en_pause': lectures_en_pause, 'search_form': search_form})

@login_required
def ajouter_livre(request, id):
    livre = get_object_or_404(Livre, id=id)
    lecteur = request.user
    lecture = Lecture(
        statut="a lire",
        livre=livre,
        lecteur=lecteur
    )
    try:
        lecture.save()
    except:
        raise PermissionDenied(f"Impossible d'ajouer une nouvelle fois le livre {livre} pour {lecteur}.")
    return redirect('livres:detail_livre', id=id)

@login_required
def supprimer_lecture(request, id):
    lecture = get_object_or_404(Lecture, id=id)

    if lecture.lecteur != request.user:
        raise PermissionDenied(f"{request.user} ne peut pas supprimer la lecture de {lecture.lecteur}.")

    lecture.delete()
    return redirect('livres:bibliotheque')

@login_required
def detail_lecture(request, id):
    lecture = get_object_or_404(Lecture, id=id)
    lecture_range = range(1, 6)
    lecture_form = MarquePagesForm(instance=lecture)
    pages_restantes = None
    if lecture.marque_pages:
        pages_restantes = lecture.livre.nombre_pages - lecture.marque_pages

    if lecture.lecteur != request.user:
        raise PermissionDenied(f"Cette lecture n'appartient pas à {{request.user}}.")

    return render(request, 'lectures/detail_lecture.html', {'lecture': lecture, 'lecture_range': lecture_range, 'form': lecture_form, "pages_restantes": pages_restantes})

@login_required
def modifier_lecture(request, id):
    lecture = get_object_or_404(Lecture, id=id)
    lecture_form = LectureForm(instance=lecture)

    if lecture.lecteur != request.user:
        raise PermissionDenied(f"Cette lecture n'appartient pas à {request.user}.")

    if request.method == 'POST':
        lecture_form = LectureForm(request.POST, instance=lecture)
        if lecture_form.has_changed() and lecture_form.is_valid():
            lecture_form.save()
            return redirect('livres:detail_lecture', id=lecture.id)
    return render(request, 'lectures/modifier_lecture.html', {'lecture': lecture, 'form': lecture_form})

@login_required
def modifier_marque_pages(request, id):
    lecture = get_object_or_404(Lecture, id=id)

    if lecture.lecteur != request.user:
        raise PermissionDenied(f"Cette lecture n'appartient pas à {request.user}.")

    if request.method == 'POST':
        lecture_form = MarquePagesForm(request.POST, instance=lecture)
        if lecture_form.is_valid():
            lecture_form.save()
            messages.success(request, "Marque-pages mis à jour avec succès !")
        else:
            messages.error(request, "Erreur lors de la mise à jour du marque-pages.")

    return redirect('livres:detail_lecture', id=lecture.id)

@login_required
def ajouter_souhait(request, id):
    livre = get_object_or_404(Livre, id=id)

    if livre not in Livre.objects.filter(user=request.user):
        request.user.liste_de_souhaits.add(livre)

    return redirect('livres:detail_livre', id=livre.id)

@login_required
def retirer_souhait(request, id):
    livre = get_object_or_404(Livre, id=id)

    if livre in Livre.objects.filter(user=request.user):
        request.user.liste_de_souhaits.remove(livre)

    return redirect('livres:detail_livre', id=livre.id)

@login_required
def liste_de_souhaits(request):
    livres = Livre.objects.filter(user=request.user)

    return render(request, 'liste_de_souhaits/liste_de_souhaits.html', {'livres': livres})
