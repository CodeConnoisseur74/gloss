from django.contrib.auth import views as auth_views
from django.urls import path

from note import views

urlpatterns = [
    path('', views.homepage, name=''),
    path('register', views.register, name='register'),
    path('my-login', views.my_login, name='my-login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('user-logout', views.user_logout, name='user-logout'),
    path('create-note', views.create_note, name='create-note'),
    path('my-notes', views.my_notes, name='my-notes'),
    path('update-note/<str:pk>', views.update_note, name='update-note'),
    path('delete-note/<str:pk>', views.delete_note, name='delete-note'),
    path('profile-management', views.profile_management, name='profile-management'),
    path('delete-account', views.delete_account, name='delete-account'),
]
