# Generated by Django 4.2.5 on 2023-10-02 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shops',
            name='loc',
            field=models.PositiveIntegerField(db_index=True, verbose_name='Локация магазина'),
        ),
        migrations.AlterField(
            model_name='shops',
            name='size',
            field=models.PositiveIntegerField(db_index=True, verbose_name='Размер магазина'),
        ),
        migrations.AlterField(
            model_name='shops',
            name='type_format',
            field=models.PositiveIntegerField(db_index=True, verbose_name='Формат магазина'),
        ),
    ]