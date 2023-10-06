from django.test import TestCase
from users.models import User

from rest_framework.test import APIClient

from api.models import Categories, Forecast, Sales, Shops


class ShopViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.shop = Shops.objects.create(name="Shop 1", location="Location 1")

    def test_list_shops(self):
        response = self.client.get('/api/shops/')  # Замените на ваш URL
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)


class ForecastViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.forecast = Forecast.objects.create(data="Your forecast data")

    def test_list_forecasts(self):
        response = self.client.get('/api/forecasts/')  # Замените на ваш URL
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)


class CategoriesViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.category = Categories.objects.create(name="Category 1")

    def test_list_categories(self):
        response = self.client.get('/api/categories/')  # Замените на ваш URL
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)


class SalesViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.sale = Sales.objects.create(date="2023-10-05", amount=100)

    def test_list_sales(self):
        response = self.client.get('/api/sales/')  # Замените на ваш URL
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
