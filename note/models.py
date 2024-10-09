from django.contrib.auth.models import User
from django.db import models


class Note(models.Model):
    """
    A model representing a note created by a user.

    Fields:
        title (CharField): The title of the note, with a maximum length of 150
        characters.
        content (CharField): The content of the note,
        with a maximum length of 400 characters.

        date_posted (DateTimeField):
        The date and time when the note was created, automatically
        set to the current timestamp.
        user (ForeignKey): A foreign key referencing the User model,
        representing the owner of the note.
        If the user is deleted, the note will be deleted (CASCADE).
    """

    title = models.CharField(max_length=150)
    content = models.CharField(max_length=400)
    date_posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User, max_length=10, on_delete=models.CASCADE, null=True
    )


class Profile(models.Model):
    """
    A model representing the user's profile.

    Fields:
        profile_pic (ImageField): The profile picture of the user,
        with a default image 'Default.png'.
        The image is uploaded to the 'media/' directory.
        user (ForeignKey): A foreign key referencing the User model,
        representing the user associated with this profile.
        If the user is deleted, the profile is also deleted (CASCADE).
    """

    profile_pic = models.ImageField(
        'image', default='Default.png', upload_to='media/'
    )
    user = models.ForeignKey(
        User, max_length=10, on_delete=models.CASCADE, null=True
    )
