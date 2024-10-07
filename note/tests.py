from django.contrib.auth.models import User
from django.test import TestCase

from note.models import Note, Profile


class NoteUserRelationshipTest(TestCase):
    def test_note_user_relationship(self):
        # Step 1: Create a test user
        user = User.objects.create_user(username='testuser', password='testpassword')

        # Step 2: Create a note and associate it with the user
        note = Note.objects.create(title='Test Note', content='This is a test note.', user=user)

        # Step 3: Verify that the note is associated with the user
        self.assertEqual(note.user, user)

        # Step 4: Check that the note is saved in the database and is associated with the correct user
        self.assertTrue(Note.objects.filter(user=user).exists())
        self.assertEqual(user.note_set.count(), 1)  # Ensure the user has one note
        self.assertEqual(user.note_set.first().title, 'Test Note')  # Verify note title
        self.assertEqual(user.note_set.first().content, 'This is a test note.')  # Verify note content


class ProfileUserRelationshipTest(TestCase):
    def test_profile_user_relationship(self):
        # Step 1: Create a test user
        user = User.objects.create_user(username='testuser', password='testpassword')

        # Step 2: Create a profile and associate it with the user
        profile = Profile.objects.create(user=user)

        # Step 3: Verify that the profile is associated with the user
        self.assertEqual(profile.user, user)

        # Step 4: Check the default profile picture
        self.assertEqual(profile.profile_pic.name, 'Default.png')

        # Step 5: Check that the profile is saved in the database and is associated with the correct user
        self.assertTrue(Profile.objects.filter(user=user).exists())
        self.assertEqual(user.profile_set.count(), 1)  # Ensure the user has one profile
