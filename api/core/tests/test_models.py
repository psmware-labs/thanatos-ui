from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email='test@psmware.io', password='testpass123'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@psmware.io'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        # Assertions
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@PSMWARE.IO'
        user = get_user_model().objects.create_user(email, 'test123')
        # Assertion
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        # Assertions
        # Here, if a value error is NOT raised, we have an error
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'superuser@psmware.io',
            'test123'
        )
        # Assertions
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
