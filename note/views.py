from django.shortcuts import render


def homepage(request):
    return render(request, 'note/index.html')


def register(request):
    return render(request, 'note/register.html')


def my_login(request):
    return render(request, 'note/my-login.html')


def dashboard(request):
    return render(request, 'note/dashboard.html')
