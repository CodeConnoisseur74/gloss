from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.shortcuts import redirect, render

from note.forms import CreateUserForm, LoginForm, NoteForm


def homepage(request):
    return render(request, 'note/index.html')


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
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
    return render(request, 'note/dashboard.html')


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

            return redirect('dashboard')

    context = {'CreateNoteForm': form}

    return render(request, 'note/create-note.html', context)
