from django.test import TestCase

from api.models import Categories, Forecast, Sales, Shops


class ShopModelTestCase(TestCase):
    def test_shop_model(self):
        shop = Shops.objects.create(
            store="Test Store",
            city="Test City",
            division="Test Division",
            type_format=1,
            loc=2,
            size=1000,
            is_active=True
        )
        self.assertEqual(
            shop.__str__(), "Test Store, Test City, Test Division"
        )


class ForecastModelTestCase(TestCase):
    def test_forecast_model(self):
        shop = Shops.objects.create(
            store="Test Store",
            city="Test City",
            division="Test Division",
            type_format=1,
            loc=2,
            size=1000,
            is_active=True
        )
        forecast = Forecast.objects.create(
            store=shop,
            forecast_date="2023-10-05",
            forecast={"key": "value"}
        )
        self.assertEqual(
            forecast.__str__(), "Test Store, 2023-10-05, {'key': 'value'}"
        )


class CategoriesModelTestCase(TestCase):
    def test_categories_model(self):
        category = Categories.objects.create(
            sku="Test SKU",
            group="Test Group",
            category="Test Category",
            subcategory="Test Subcategory",
            uom=10
        )
        self.assertEqual(
            category.__str__(),
            "Test Group - Test Category - Test Subcategory - Test SKU"
        )


class SalesModelTestCase(TestCase):
    def test_sales_model(self):
        shop = Shops.objects.create(
            store="Test Store",
            city="Test City",
            division="Test Division",
            type_format=1,
            loc=2,
            size=1000,
            is_active=True
        )
        category = Categories.objects.create(
            sku="Test SKU",
            group="Test Group",
            category="Test Category",
            subcategory="Test Subcategory",
            uom=10
        )
        sales = Sales.objects.create(
            store=shop,
            sku=category,
            date="2023-10-05",
            sales_type=1,
            sales_units=100,
            sales_units_promo=50,
            sales_rub=500.50,
            sales_run_promo=250.25
        )
        self.assertEqual(sales.__str__(), "Test Store - Test SKU")
