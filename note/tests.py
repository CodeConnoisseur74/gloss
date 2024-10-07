from django.contrib.auth.models import User
from django.test import TestCase

from note.models import Note


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
