from django import forms
from api.models import Livre, Auteur, Tag

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
            'serie': forms.Select(attrs={
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
