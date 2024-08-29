from django.test import TestCase
import unittest
from django.core.exceptions import ValidationError
from users.models import User


class UserModelTest(TestCase):
    def test_user_creation(self):

        user = User.objects.create_user(username='testuser', email='test@example.com', password='password')

        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_invalid_user_creation(self):
        with self.assertRaises(ValueError):
            User.objects.create_user(email='test@example.com', password='password')

    def test_login(self):
        user = User.objects.create_user(username='testuser2', email='test2@example.com', password='password')
        self.client.login(username='testuser2', password='password')

        response = self.client.get('/')
        self.assertIn('Hello, testuser2!', response.content.decode())


class UserTest(TestCase):
    def setUp(self):
        self.user_data = {
            'email': '<test@test.com>',
            'token': 'abcdefg',
        }

    def test_user_creation(self):
        user = User.objects.create(**self.user_data)
        self.assertEqual(user.email, self.user_data['email'])
        self.assertIsNotNone(user.token)

    def test_unique_email(self):
        user = User.objects.create(**self.user_data)
        with self.assertRaises(ValidationError):
            User.objects.create(email=user.email)

    def test_required_fields(self):

        with self.assertRaises(ValidationError):
            User.objects.create(email=None)

        user = User.objects.create(email=self.user_data['email'])
        self.assertIsNone(user.token)

    def test_str_representation(self):
        user = User.objects.create(**self.user_data)
        self.assertEqual(str(user), user.email)
