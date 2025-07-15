from django import forms
from api.models import Livre, Auteur, Tag, Lecture

class LivreForm(forms.ModelForm):
    auteurs = forms.ModelMultipleChoiceField(
        queryset=Auteur.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=True
    )

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=True
    )

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
            'synopsis': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'edition': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'isbn': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            })
        }
        labels = {
            'isbn': 'ISBN'
        }

    def __init__(self, *args, **kwargs):
        super(LivreForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk and self.instance.date_sortie:
            self.initial['date_sortie'] = self.instance.date_sortie.strftime('%Y-%m-%d')

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
            }),
            'biographie': forms.Textarea(attrs={
                'class': 'form-control'
            })
        }

    def __init__(self, *args, **kwargs):
        super(AuteurForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk and self.instance.date_naissance:
            self.initial['date_naissance'] = self.instance.date_naissance.strftime('%Y-%m-%d')
        if self.instance and self.instance.pk and self.instance.date_mort:
            self.initial['date_mort'] = self.instance.date_mort.strftime('%Y-%m-%d')

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'

        widgets = {
            'tag': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'pour_adulte': forms.CheckboxInput(attrs={
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
        fields = ['date_debut', 'date_fin', 'statut', 'note', 'marque_pages', 'commentaire']
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
            'statut': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'note': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'commentaire': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
            'marque_pages': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }
        labels = {
            'date_debut': 'Date de début',
            'date_fin': 'Date de fin',
            'statut': 'Statut de lecture',
            'note': 'Note',
            'commentaire': 'Commentaire',
            'marque_pages': 'Marque-pages',
        }

    def __init__(self, *args, **kwargs):
        super(LectureForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk and self.instance.date_debut:
            self.initial['date_debut'] = self.instance.date_debut.strftime('%Y-%m-%d')
        if self.instance and self.instance.pk and self.instance.date_fin:
            self.initial['date_fin'] = self.instance.date_fin.strftime('%Y-%m-%d')

class MarquePagesForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ['marque_pages']
        widgets = {
            'marque_pages': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }
