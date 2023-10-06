from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


class UserModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword',
            first_name='Test',
            last_name='User'
        )

    def test_create_user(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertEqual(self.user.first_name, 'Test')
        self.assertEqual(self.user.last_name, 'User')
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)

    def test_create_superuser(self):
        admin_user = get_user_model().objects.create_superuser(
            username='adminuser',
            email='admin@example.com',
            password='adminpassword'
        )
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

    # def test_unique_username(self):
    #     with self.assertRaises(ValidationError):
    #         get_user_model().objects.create_user(
    #             username='testuser',
    #             email='another@example.com',
    #             password='testpassword',
    #             first_name='Another',
    #             last_name='User'
    #         )

    def test_get_full_name(self):
        self.assertEqual(self.user.get_full_name(), 'Test User')

    def test_get_short_name(self):
        self.assertEqual(self.user.get_short_name(), 'testuser')

    def test_user_string_representation(self):
        self.assertEqual(str(self.user), 'testuser')

    # def test_user_clean_method(self):
    #     # Попробуем создать пользователя с уже существующим именем
    #     with self.assertRaises(ValidationError):
    #         get_user_model().objects.create_user(
    #             username='testuser',
    #             email='another@example.com',
    #             password='testpassword',
    #             first_name='Another',
    #             last_name='User'
    #         )
