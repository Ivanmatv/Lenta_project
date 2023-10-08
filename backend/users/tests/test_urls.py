from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from users.views import CustomUserViewSet

class UrlsTestCase(TestCase):
    def setUp(self):
        # Создаем пользователя и получаем токен доступа для аутентификации
        self.user = CustomUser.objects.create(username='testuser')
        self.user.set_password('testpassword')
        self.user.save()
        self.token = Token.objects.create(user=self.user)

        # Создаем клиент API и устанавливаем заголовок авторизации с токеном
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

    def test_users_url_resolves(self):
        url = reverse('users-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.resolver_match.func.cls, CustomUserViewSet)

    def test_v1_url_includes_djoser_urls(self):
        url = reverse('users-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.resolver_match.app_name, 'v1')

    def test_auth_url_includes_djoser_authtoken_urls(self):
        url = reverse('token_login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.resolver_match.app_name, 'v1')

    def test_auth_url_includes_djoser_jwt_urls(self):
        url = reverse('jwt_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.resolver_match.app_name, 'v1')

