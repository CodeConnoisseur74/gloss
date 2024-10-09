"""
Forms for the 'note' app.

This module defines several forms used in the app, including:
    - NoteForm: Handles note creation and editing.
    - CreateUserForm: Manages user registration with the required fields.
    - LoginForm: Manages user authentication with a custom login form.
    - UpdateUserForm: Allows users to update their account information
        (username and email).
    - UpdateProfileForm: Allows users to update their profile picture.
"""

from typing import ClassVar

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.forms.widgets import PasswordInput, TextInput

from note.models import Note, Profile


class NoteForm(ModelForm):
    """
    Form to create or update a note. Excludes the 'user' field which is set
    programmatically.
    """

    class Meta:
        model = Note
        fields: ClassVar[list[str]] = ['title', 'content']
        exclude: ClassVar[list[str]] = ['user']


class CreateUserForm(UserCreationForm):
    """
    Form for registering a new user. Includes fields for username, email,
    password1, and
    password2.
    """

    class Meta:
        model = User
        fields: ClassVar[list[str]] = [
            'username',
            'email',
            'password1',
            'password2',
        ]


class LoginForm(AuthenticationForm):
    """
    Custom login form using Django's AuthenticationForm with customized
    username and password fields.
    """

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


class UpdateUserForm(forms.ModelForm):
    """
    Form to update a user's account information (username and email).
    Password fields are excluded.
    """

    password = None

    class Meta:
        model = User
        fields: ClassVar[list[str]] = ['username', 'email']
        exclude: ClassVar[list[str]] = ['password1', 'password2']


class UpdateProfileForm(forms.ModelForm):
    """
    Form to update a user's profile picture. Uses a custom file input widget
    for the profile_pic field.

    """

    profile_pic = forms.ImageField(
        widget=forms.FileInput(attrs={'class': 'form-control-file'})
    )

    class Meta:
        model = Profile
        fields: ClassVar[list[str]] = ['profile_pic']
