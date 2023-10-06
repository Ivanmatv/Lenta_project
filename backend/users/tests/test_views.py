from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User


class CustomUserViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword',
            first_name='Test',
            last_name='User'
        )
        self.refresh = RefreshToken.for_user(self.user)
        self.client.force_authenticate(user=self.user)

    def test_user_info(self):
        url = reverse('users:users')  # Подставьте правильное имя маршрута
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user_data']['username'], 'testuser')

    def test_user_info_unauthenticated(self):
        self.client.logout()
        url = reverse('/api/users/user_data/')  # Подставьте правильное имя маршрута
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
