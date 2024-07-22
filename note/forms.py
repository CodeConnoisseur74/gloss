from typing import ClassVar

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.forms.widgets import PasswordInput, TextInput

from note.models import Note


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields: ClassVar[list[str]] = ['title', 'content']
        exclude: ClassVar[list[str]] = ['user']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields: ClassVar[list[str]] = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
