from random import randint
from django.db.models import Max
from django.shortcuts import render, redirect
from .forms import LecteurForm
from api.models import Livre

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
        form = LecteurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = LecteurForm()
    return render(request, 'auth/signup.html', {'form': form})
