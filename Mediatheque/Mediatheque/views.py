from random import randint
from django.db.models import Max
from django.shortcuts import render, redirect
from .forms import UserForm, UserUpdateForm, CustomPasswordChangeForm
from api.models import Livre
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash

def hub(request):
    max_id = Livre.objects.aggregate(max_id=Max('id'))['max_id']
    if max_id:
        random_id = randint(1, max_id)
        livre = Livre.objects.filter(id=random_id).first()
    else:
        livre = None
    return render(request, 'hub.html', {'livre': livre})

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserForm()
    return render(request, 'auth/signup.html', {'form': form})

@login_required
def account(request):
    return render(request, 'user/account.html')

@login_required
def modifier_utilisateur(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('account')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'user/modifier_account.html', {'form': form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('account')
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'user/change_password.html', {'form': form})
