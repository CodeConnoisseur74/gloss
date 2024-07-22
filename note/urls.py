from django.urls import path

from note import views

urlpatterns = [
    path('', views.homepage, name=''),
    path('register', views.register, name='register'),
    path('my-login', views.my_login, name='my-login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('user-logout', views.user_logout, name='user-logout'),
    path('create-note', views.create_note, name='create-note'),
    path('my-notes', views.create_note, name='my-notes'),
]
