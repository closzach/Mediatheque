from django import forms
from django.contrib.auth.forms import UserCreationForm
from api.models import Lecteur

class LecteurForm(UserCreationForm):
    date_naissance = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control'
        }),
        label="Date de naissance"
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'type': 'pass',
            'class': 'form-control'
        }),
        label="Mot de passe"
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'type': 'pass',
            'class': 'form-control'
        }),
        label="Confirmation du mot de passe"
    )

    class Meta:
        model = Lecteur
        fields = ['username', 'date_naissance', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'form-control'
            })
        }
