"""
Views for the 'note' app.

This module defines the views that handle various operations such as:
    - User registration, login, and logout
    - Note creation, updating, and deletion
    - Profile management and account deletion
    - Password reset and management

Each view corresponds to a specific URL pattern in the 'note' app and is responsible
for rendering the corresponding HTML template and handling form submissions or other requests.

Views:
    - homepage: Displays the homepage of the app.
    - register: Handles user registration and form submissions.
    - my_login: Manages the login functionality.
    - dashboard: Displays the user dashboard after login.
    - user_logout: Logs out the current user and redirects to the homepage.
    - create_note: Allows users to create a new note.
    - my_notes: Displays a list of notes created by the user.
    - update_note: Allows users to update an existing note.
    - delete_note: Handles the deletion of a note by the user.
    - profile_management: Manages the user's profile information.
    - delete_account: Handles the deletion of a users account.
"""

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from note.forms import CreateUserForm, LoginForm, NoteForm, UpdateProfileForm, UpdateUserForm
from note.models import Note, Profile


def homepage(request):
    """
    View to display the homepage of the application.
    """
    return render(request, 'note/index.html')


def register(request):
    """
    Manages the login process. Displays the login form and processes the login action.
    """
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            current_user = form.save(commit=False)
            form.save()
            send_mail(
                'Welcome to Gloss',
                'Congrats on creating your account!',
                settings.DEFAULT_FROM_EMAIL,
                [current_user.email],
            )
            profile = Profile.objects.create(user=current_user)
            messages.success(request, 'User created!')
            return redirect('my-login')

    context = {'RegistrationForm': form}
    return render(request, 'note/register.html', context)


def my_login(request):
    """
    Manages the login process. Displays the login form and processes the login action.
    """
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
    context = {'LoginForm': form}
    return render(request, 'note/my-login.html', context)


def user_logout(request):
    """
    Logs out the current user and redirects them to the homepage.
    """
    auth.logout(request)
    messages.success(request, 'You were logged out seccessfully!')
    return redirect('')


@login_required(login_url='my-login')
def dashboard(request):
    """
    Displays the dashboard view for authenticated users.
    """
    profile_pic = Profile.objects.get(user=request.user)
    context = {'profilePic': profile_pic}
    return render(request, 'note/dashboard.html', context)


@login_required(login_url='my-login')
def create_note(request):
    """
    Allows users to create a new note. Displays the form and processes submissions.
    """
    form = NoteForm()

    if request.method == 'POST':
        form = NoteForm(request.POST)

        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            messages.success(request, 'Note created!')
            return redirect('my-notes')
    context = {'CreateNoteForm': form}
    return render(request, 'note/create-note.html', context)


@login_required(login_url='my-login')
def my_notes(request):
    """
    Displays a list of notes created by the authenticated user.
    """
    current_user = request.user.id
    notes = Note.objects.filter(user=current_user).order_by('-date_posted')
    context = {'AllNotes': notes}
    return render(request, 'note/my-notes.html', context)


@login_required(login_url='my-login')
def update_note(request, pk):
    """
    Allows users to update an existing note identified by its primary key (pk).
    """
    try:
        note = Note.objects.get(id=pk, user=request.user)
    except:  # noqa: E722
        return redirect('my-notes')

    form = NoteForm(instance=note)

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)

        if form.is_valid():
            form.save()
            messages.success(request, 'Note updated!')

            return redirect('my-notes')
    context = {'UpdateNote': form}
    return render(request, 'note/update-note.html', context)


@login_required(login_url='my-login')
def profile_management(request):
    """
    Manages the user's profile, allowing them to update their profile information.
    """
    form = UpdateUserForm(instance=request.user)
    profile = Profile.objects.get(user=request.user)
    form_2 = UpdateProfileForm(instance=profile)

    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user)
        form_2 = UpdateProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            form.save()
            messages.success(request, 'Update success!')
            return redirect('dashboard')

        if form_2.is_valid():
            form_2.save()

            messages.success(request, 'Update success!')
            return redirect('dashboard')
    context = {'UserUpdateForm': form, 'ProfileUpdateForm': form_2}
    return render(request, 'note/profile-management.html', context)


@login_required(login_url='my-login')
def delete_account(request):
    """
    Handles the deletion of a user's account. Displays a confirmation and processes account deletion.
    """
    if request.method == 'POST':
        delete_user = User.objects.get(username=request.user)
        delete_user.delete()
        messages.success(request, 'Your account was deleted!')

        return redirect('')
    return render(request, 'note/delete-account.html')


@login_required(login_url='my-login')
def delete_note(request, pk):
    try:
        note = Note.objects.get(id=pk, user=request.user)
    except:  # noqa: E722
        return redirect('my-notes')

    if request.method == 'POST':
        note.delete()
        messages.success(request, 'Note deleted!')
        return redirect('my-notes')

    return render(request, 'note/delete-note.html')
