from django import forms
from api.models import Livre, Auteur, Tag, Lecture

class LivreForm(forms.ModelForm):
    class Meta:
        model = Livre
        fields = '__all__'

        widgets = {
            'nom': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'date_sortie': forms.DateInput(attrs={
                'class':'form-control',
                'type': 'date'
            }),
            'nombre_pages': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'isbn': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'auteurs': forms.SelectMultiple(attrs={
                'class': 'form-control'
            }),
            'tags': forms.SelectMultiple(attrs={
                'class': 'form-control'
            })
        }

class AuteurForm(forms.ModelForm):
    class Meta:
        model = Auteur
        fields = '__all__'

        widgets = {
            'nom': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'date_naissance': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'date_mort': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            })
        }

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'

        widgets = {
            'tag': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'nsfw': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'modifiable': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }

class SearchForm(forms.Form):
    recherche = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Rechercher',
            'aria-label': 'Rechercher',
            'aria-describedby': 'search-button'
        })
    )

class SearchLivreForm(forms.Form):
    recherche = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Rechercher',
            'aria-label': 'Rechercher',
            'aria-describedby': 'search-button'
        })
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple(
            attrs={
                'class': 'form-check-input'
            }
        )
    )
    auteur = forms.ModelChoiceField(
        queryset=Auteur.objects.all(),
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-select',
        })
    )

class SearchLectureForm(forms.Form):
    recherche = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Rechercher',
            'aria-label': 'Rechercher',
            'aria-describedby': 'search-button'
        })
    )
    statut = forms.ChoiceField(
        choices=[
            ('', ''),
            ('a lire', 'À lire'),
            ('lu', 'Lu'),
            ('en cours', 'En cours'),
            ('abandonne', 'Abandonné'),
            ('en pause', 'En pause')
        ],
        label="Statut",
        widget=forms.Select(attrs={
            'class': 'form-control'
        }),
        required=False
    )

class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ['date_debut', 'date_fin', 'statut', 'note']
        widgets = {
            'date_debut': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),
            'date_fin': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),
            'statut': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'note': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            )
        }
        labels = {
            'date_debut': 'Date de début',
            'date_fin': 'Date de fin',
            'statut': 'Statut de lecture',
            'note': 'Note',
        }

    STATUT_CHOICES = [
        ('a lire', 'À lire'),
        ('lu', 'Lu'),
        ('en cours', 'En cours'),
        ('abandonne', 'Abandonné'),
        ('en pause', 'En pause'),
    ]
    statut = forms.ChoiceField(
        choices=STATUT_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Statut de lecture'
    )
