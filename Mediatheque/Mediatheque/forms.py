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

    class Meta:
        model = Lecteur
        fields = ['username', 'date_naissance', 'password1', 'password2']
