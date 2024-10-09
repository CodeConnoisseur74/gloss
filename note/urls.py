"""
URL configuration for the 'note' app.

This module defines URL patterns for the note app, including routes for user authentication,
password management, note management, and profile management. The paths correspond to view functions
in the 'note' app and Django's built-in authentication views.

The URLs include:
    - User registration, login, and logout
    - Dashboard and note-related actions (create, update, delete)
    - Profile management and account deletion
    - Password reset and management views (reset, confirm, complete)

Routes:
    - '' (homepage): Maps to the homepage view.
    - 'register': Maps to the user registration view.
    - 'my-login': Maps to the user login view.
    - 'dashboard': Maps to the user's dashboard view.
    - 'user-logout': Maps to the logout functionality.
    - 'create-note': Maps to the view for creating a new note.
    - 'my-notes': Maps to the view displaying the user's notes.
    - 'update-note/<str:pk>': Maps to the view for updating a note (identified by primary key).
    - 'delete-note/<str:pk>': Maps to the view for deleting a note (identified by primary key).
    - 'profile-management': Maps to the profile management view.
    - 'delete-account': Maps to the view for deleting the user's account.
    - Password reset routes provided by Django's authentication views for resetting user passwords.
"""

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
    # Password management
    # 1 - Allow users to enter their email in order to receive a password reset link
    path(
        'reset_password',
        auth_views.PasswordResetView.as_view(template_name='note/password-reset.html'),
        name='reset_password',
    ),
    # 2 - Display a success message stating that an email was sent to reset the password
    path(
        'reset_password_sent',
        auth_views.PasswordResetDoneView.as_view(template_name='note/password-reset-sent.html'),
        name='password_reset_done',
    ),
    # 3 - Handle the password reset link sent to the user's email
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='note/password-reset-form.html'),
        name='password_reset_confirm',
    ),
    # 4 - Show a success message once the password has been changed
    path(
        'password_reset_complete',
        auth_views.PasswordResetCompleteView.as_view(template_name='note/password-reset-complete.html'),
        name='password_reset_complete',
    ),
]
