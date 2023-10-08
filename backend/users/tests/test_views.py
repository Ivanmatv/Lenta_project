# import json
# from django.test import TestCase
# from rest_framework.test import APIRequestFactory
# from rest_framework.authtoken.models import Token
# from django.contrib.auth.models import User
# from rest_framework import status
# from users.models import User
# from users.serializers import CustomUserSerializer
# from users.views import CustomUserViewSet


# class ViewsTestCase(TestCase):
#     def setUp(self):
#         self.factory = APIRequestFactory()
#         self.user = User.objects.create(username='testuser', email='testuser@example.com')
#         self.token = Token.objects.create(user=self.user)

#     def test_user_viewset(self):
#         view = CustomUserViewSet.as_view({'get': 'list'})
#         request = self.factory.get('/api/users/')
#         request.auth = self.token  # Аутентификация с использованием токена
#         response = view(request)
#         self.assertEqual(response.status_code, 200)

#     def test_user_info_action(self):
#         view = CustomUserViewSet.as_view({'get': 'user_info'})
#         request = self.factory.get('/api/users/user_info/')
#         request.auth = self.token  # Аутентификация с использованием токена
#         response = view(request)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertIn('token', response.data)
#         self.assertIn('user_data', response.data)

#     def test_user_info_action_unauthenticated(self):
#         view = CustomUserViewSet.as_view({'get': 'user_info'})
#         request = self.factory.get('/api/users/user_info/')
#         response = view(request)
#         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
