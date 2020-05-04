from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import UserRegisterForm, UserEditForm, ProfileEditForm, UserDeleteForm
from .templatetags.eligible import is_eligible
from .templatetags.bizzfuzz import bizz_or_fuzz
import csv


def users_list(request):
    context = {'users': User.objects.all(), 'title': 'Users list'}
    return render(request, 'test_case/users_list.html', context)


def user_profile(request, profile_name):
    context = {'user': User.objects.filter(username=profile_name).first(), 'title': f'{profile_name} Profile'}
    return render(request, 'test_case/user_profile.html', context)


def user_create(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.birthday = form.cleaned_data.get('birthday')
            user.save()
            return redirect('users-list')
    else:
        form = UserRegisterForm()
    context = {'form': form, 'title': 'Create New User'}
    return render(request, 'test_case/user_create.html', context)


def user_edit(request, profile_name):
    user = User.objects.filter(username=profile_name).first()
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=user)
        profile_form = ProfileEditForm(request.POST, instance=user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('user-profile', profile_name=user.username)
    else:
        user_form = UserEditForm(instance=user)
        profile_form = ProfileEditForm(instance=user.profile)
    context = {'user_form': user_form, 'profile_form': profile_form, 'title': f'Edit {profile_name} Profile'}
    return render(request, 'test_case/user_edit.html', context)


def user_delete(request, profile_name):
    user = User.objects.filter(username=profile_name).first()
    if request.method == 'POST':
        form = UserDeleteForm(request.POST, instance=user)
        if form.is_valid():
            user.delete()
            return redirect('users-list')
    else:
        form = UserDeleteForm(instance=user)
    context = {'user': user, 'form': form, 'title': f'Delete {profile_name} Profile'}
    return render(request, 'test_case/user_delete.html', context)


def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'

    writer = csv.writer(response)
    users = User.objects.all()

    writer.writerow(['Username', 'Birthday', 'Eligible', 'Random Number', 'BizzFuzz'])
    for user in users:
        writer.writerow(
            [
                user.username,
                user.profile.birthday.strftime('%-m/%-d/%Y'),
                is_eligible(user.profile.birthday),
                user.profile.number,
                bizz_or_fuzz(user.profile.number),
            ]
        )

    return response
