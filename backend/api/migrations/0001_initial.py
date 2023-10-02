# Generated by Django 4.2.5 on 2023-10-02 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shops',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store', models.CharField(db_index=True, max_length=100, verbose_name='Магазин')),
                ('city', models.CharField(db_index=True, max_length=100, verbose_name='Город')),
                ('division', models.CharField(db_index=True, max_length=100, verbose_name='Дивизион')),
                ('type_format', models.IntegerField(db_index=True, verbose_name='Формат магазина')),
                ('loc', models.IntegerField(db_index=True, verbose_name='Локация магазтна')),
                ('size', models.IntegerField(db_index=True, verbose_name='Размер магазина')),
                ('is_active', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Торговый комплекс',
                'verbose_name_plural': 'Тороговые комплексы',
                'ordering': ('store',),
            },
        ),
        migrations.CreateModel(
            name='Forecast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forecast_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('forecast', models.JSONField()),
                ('store', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.shops')),
            ],
            options={
                'verbose_name': 'Прогноз',
                'verbose_name_plural': 'Прогнозы',
            },
        ),
    ]