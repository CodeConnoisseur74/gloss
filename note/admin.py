from django.contrib import admin

from note.models import Note, Profile

"""
Registers the Note and Profile models with the Django admin site.

By registering these models, they become available in the Django
admin interface, allowing administrators to view, add, modify,
and delete instances of the Note and Profile models.
"""


admin.site.register(Note)
admin.site.register(Profile)
