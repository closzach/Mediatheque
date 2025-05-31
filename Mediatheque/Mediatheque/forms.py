from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from api.models import User

class UserForm(UserCreationForm):
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
        model = User
        fields = ['username', 'date_naissance', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'form-control'
            })
        }
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk and self.instance.date_naissance:
            self.initial['date_naissance'] = self.instance.date_naissance.strftime('%Y-%m-%d')

class UserUpdateForm(forms.ModelForm):
    date_naissance = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control'
        }),
        label="Date de naissance"
    )

    cacher_pour_adulte = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input'
        }),
        label="Cacher les contenus pour adulte",
        required=False
    )

    class Meta:
        model = User
        fields = ['username', 'date_naissance', 'cacher_pour_adulte']

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk and self.instance.date_naissance:
            self.initial['date_naissance'] = self.instance.date_naissance.strftime('%Y-%m-%d')
        self.fields['username'].widget.attrs.update({'class': 'form-control'})

class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'class': 'form-control'})
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control'})
