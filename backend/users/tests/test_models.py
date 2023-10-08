from django.test import TestCase
from django.core.exceptions import ValidationError
from users.models import User

class UserModelTest(TestCase):
    def test_create_user(self):
        # Создаем пользователя
        user = User.objects.create_user(
            username='testuser1',  # Уникальное имя пользователя
            email='test@example.com',
            password='testpassword',
            first_name='John',
            last_name='Doe'
        )

        # Проверяем, что пользователь создан корректно
        self.assertEqual(user.username, 'testuser1')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        # Создаем суперпользователя
        superuser = User.objects.create_superuser(
            username='admin1',  # Уникальное имя пользователя
            email='admin@example.com',
            password='adminpassword',
            first_name='Admin',
            last_name='User'
        )

        # Проверяем, что суперпользователь создан корректно
        self.assertEqual(superuser.username, 'admin1')
        self.assertEqual(superuser.email, 'admin@example.com')
        self.assertEqual(superuser.first_name, 'Admin')
        self.assertEqual(superuser.last_name, 'User')
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

    def test_create_user_without_email(self):
        # Попытка создать пользователя без email должна вызывать ошибку
        with self.assertRaises(ValueError):
            User.objects.create_user(
                username='testuser2',  # Уникальное имя пользователя
                email='test@emai.com',
                password='testpassword',
                first_name='John',
                last_name='Doe'
            )

    def test_create_user_without_username(self):
        # Попытка создать пользователя без username должна вызывать ошибку
        with self.assertRaises(ValueError):
            User.objects.create_user(
                email='test2@example.com',  # Уникальный email
                emai='test2@mail.com',
                password='testpassword',
                first_name='John',
                last_name='Doe'
            )

    def test_duplicate_username(self):
        # Попытка создать пользователя с уже существующим именем пользователя должна вызывать ошибку
        User.objects.create_user(
            username='testuser3',  # Уникальное имя пользователя
            email='test@example.com',
            password='testpassword',
            first_name='John',
            last_name='Doe'
        )
        with self.assertRaises(ValidationError):
            User.objects.create_user(
                username='testuser3',  # Повторяющееся имя пользователя
                email='another@example.com',  # Уникальный email
                password='anotherpassword',
                first_name='Jane',
                last_name='Doe'
            )
