"""
.. module:: test_superuser
"""

from django.contrib.auth.models import User
from django.test import Client
from django.test import TestCase


class TestUserCreatedWithManagePyCreatesuperuser(TestCase):
    """
    Check if user created with "manage.py createsuperuser"
    can log in and see own profile.
    """
    @classmethod
    def setUpTestData(cls):
        cls.superuser_data = {
            'username': 'test_admin',
            'password': 'secret',
            'email': 'test_admin@example.com'
        }
        User.objects.create_superuser(**cls.superuser_data)

    def setUp(self):
        self.client = Client()

    def test_log_into_admin_panel(self):
        """Check if user can log into admin panel."""
        response = self.client.post(
            '/admin/login/',
            {
                'username': self.superuser_data['username'],
                'password': self.superuser_data['password'],
                'next': '/admin/login/',
            },
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Wyloguj się')

    def test_failed_log_into_admin_panel(self):
        """Check if user can log into admin panel using invalid credentials."""
        response = self.client.post(
            '/admin/login/',
            {
                'username': self.superuser_data['username'],
                'password': self.superuser_data['password'] + 'invalid',
                'next': '/admin/login/',
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            'Wprowadź poprawne dane w polach &quot;użytkownik&quot;'
            ' i &quot;hasło&quot; dla konta należącego do zespołu.'
            ' Uwaga: wielkość liter może mieć znaczenie.',
        )

    def test_log_into_admin_panel_and_go_to_logged_user_profile_view(self):
        """
        Check if user can log into admin panel and then see
        own profile page (logged_user_profile view).
        """
        self.client.post(
            '/admin/login/',
            {
                'username': self.superuser_data['username'],
                'password': self.superuser_data['password'],
                'next': '/admin/login/',
            },
        )
        response = self.client.get('/me')
        self.assertEqual(response.status_code, 200)
