from random import randint
from django.db.models import Max
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm, UserUpdateForm, CustomPasswordChangeForm
from api.models import Livre, User
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.contrib.auth.models import Group
from django.contrib import messages
from django.http import JsonResponse

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

@login_required
def supprimer_account(request):
    if request.method == 'POST':
        request.user.delete()
        redirect('hub')
    return redirect(reverse('account'))

@permission_required('auth.view_group')
def group_list(request):
    groups = Group.objects.all().prefetch_related('user_set', 'permissions')
    context = {
        'groups': groups,
    }
    return render(request, 'admin/group_list.html', context)

@permission_required('auth.change_group')
def manage_group_users(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    users_in_group = group.user_set.all()
    users_not_in_group = User.objects.exclude(groups=group)
    
    context = {
        'group': group,
        'users_in_group': users_in_group,
        'users_not_in_group': users_not_in_group,
    }
    return render(request, 'admin/manage_group_users.html', context)

@require_POST
@permission_required('auth.change_group')
def add_user_to_group(request, group_id, user_id):
    group = get_object_or_404(Group, id=group_id)
    user = get_object_or_404(User, id=user_id)
    
    if user not in group.user_set.all():
        group.user_set.add(user)
        messages.success(request, f'{user.username} ajouté au groupe {group.name}')
    else:
        messages.warning(request, f'{user.username} est déjà dans le groupe {group.name}')
    
    return redirect('manage_group_users', group_id=group_id)

@require_POST
@permission_required('auth.change_group')
def remove_user_from_group(request, group_id, user_id):
    group = get_object_or_404(Group, id=group_id)
    user = get_object_or_404(User, id=user_id)
    
    if user in group.user_set.all():
        group.user_set.remove(user)
        messages.success(request, f'{user.username} retiré du groupe {group.name}')
    else:
        messages.warning(request, f'{user.username} n\'est pas dans le groupe {group.name}')
    
    return redirect('manage_group_users', group_id=group_id)

@require_POST
@permission_required('auth.change_group')
def ajax_toggle_user_group(request, group_id, user_id):
    group = get_object_or_404(Group, id=group_id)
    user = get_object_or_404(User, id=user_id)
    
    if user in group.user_set.all():
        group.user_set.remove(user)
        action = 'removed'
        message = f'{user.username} retiré du groupe {group.name}'
    else:
        group.user_set.add(user)
        action = 'added'
        message = f'{user.username} ajouté au groupe {group.name}'
    
    return JsonResponse({
        'success': True,
        'action': action,
        'message': message,
        'user_id': user_id,
        'group_id': group_id
    })
