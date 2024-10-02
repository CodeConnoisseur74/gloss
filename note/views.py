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
    return render(request, 'note/index.html')


def register(request):
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
    auth.logout(request)
    messages.success(request, 'You were logged out securely!')
    return redirect('')


@login_required(login_url='my-login')
def dashboard(request):
    profile_pic = Profile.objects.get(user=request.user)
    context = {'profilePic': profile_pic}
    return render(request, 'note/dashboard.html', context)


@login_required(login_url='my-login')
def create_note(request):
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
    current_user = request.user.id
    notes = Note.objects.filter(user=current_user).order_by('-date_posted')
    context = {'AllNotes': notes}
    return render(request, 'note/my-notes.html', context)


@login_required(login_url='my-login')
def update_note(request, pk):
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
