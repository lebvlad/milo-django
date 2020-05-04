from django import forms
from datetime import date
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    birthday = forms.DateField(widget=forms.widgets.DateInput(format=('%Y-%m-%d'), attrs={"type": "date"}))

    class Meta:
        model = User
        fields = ['username', 'birthday', 'password1', 'password2']


class UserEditForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['username']


class ProfileEditForm(forms.ModelForm):
    birthday = forms.DateField(widget=forms.widgets.DateInput(format=('%Y-%m-%d'), attrs={"type": "date"}))
    number = forms.IntegerField()

    class Meta:
        model = Profile
        fields = ['birthday', 'number']


class UserDeleteForm(forms.ModelForm):
    class Meta:
        model = User
        fields = []
