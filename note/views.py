from django.shortcuts import redirect, render

from note.forms import CreateUserForm


def homepage(request):
    return render(request, 'note/index.html')


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my-login')
    context = {'RegistrationForm': form}
    return render(request, 'note/register.html')


def my_login(request):
    return render(request, 'note/my-login.html')


def dashboard(request):
    return render(request, 'note/dashboard.html')
