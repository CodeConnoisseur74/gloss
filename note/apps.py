from django.apps import AppConfig

"""
Configuration class for the 'note' Django application.

This class defines settings and configurations for the 'note'
app, such as the default auto field type and the application
name, which is used by Django to register and manage the app.
"""


class NoteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'note'
