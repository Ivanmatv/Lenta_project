from django.db import models


class Shops(models.Model):
    """Модель торгового комплекса."""
    store = models.CharField(
        'Магазин',
        max_length=100,
        db_index=True
    )
    city = models.CharField('Город', max_length=100)
    division = models.CharField('Дивизион', max_length=100)
    type_format = models.IntegerField()
    loc = models.IntegerField()
    size = models.IntegerField()
    is_active = models.BooleanField()

    class Meta:
        ordering = ('store',)
        verbose_name = 'Торговый комплекс'
        verbose_name_plural = 'Тороговые комплексы'

    def __str__(self):
        return (
            self.store,
            self.city,
            self.division
        )


class Categories(models.Model):
    """Модель товарной иерархии."""
    sku = models.CharField('Товар', max_length=100)
    group = models.CharField('Группа', max_length=100)
    category = models.CharField('Категория', max_length=100)
    subcategory = models.CharField('Подкатегория', max_length=100)
    uom = models.IntegerField()

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return (
            self.sku,
            self.group,
            self.category,
            self.subcategory
        )


class Forecast(models.Model):
    """Модель прогноза."""
    store = models.ForeignKey(Shops, on_delete=models.CASCADE)
    forecast_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    forecast = models.JSONField()

    class Meta:
        verbose_name = 'Прогноз'
        verbose_name_plural = 'Прогнозы'

    def __str__(self):
        return (
            self.store,
            self.forecast_date,
            self.forecast
        )


class Sales(models.Model):
    """Модель с информацией о количестве проданных товаров."""
    store = models.ForeignKey(
        Shops, on_delete=models.CASCADE
    )
    sku = models.ForeignKey(
        Categories, on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Информация'
        verbose_name_plural = 'Информации'

    def __str__(self):
        return (
            self.store,
            self.sku
        )


class SalesEntry(models.Model):
    sales = models.ForeignKey(
        Sales, related_name='fact', on_delete=models.CASCADE
    )
    date = models.DateField()
    sales_type = models.IntegerField()
    sales_units = models.IntegerField()
    sales_units_promo = models.IntegerField()
    sales_rub = models.DecimalField(max_digits=10, decimal_places=2)
    sales_run_promo = models.DecimalField(max_digits=10, decimal_places=2)
