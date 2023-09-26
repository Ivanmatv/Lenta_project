from django.db import models


class Shops(models.Model):
    """Модель торгового комплекса."""
    store = models.CharField('Магазин', max_length=100)
    city = models.CharField('Город', max_length=100)
    division = models.CharField('Дивизион', max_length=100)

    class Meta:
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
    forecast = models.ForeignKey(Categories, on_delete=models.CASCADE)

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
