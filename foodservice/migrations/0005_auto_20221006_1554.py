# Generated by Django 3.2.13 on 2022-10-06 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodservice', '0004_merge_0002_auto_20221006_0908_0003_auto_20221006_1200'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='allergen',
            options={'verbose_name': 'аллерген', 'verbose_name_plural': 'аллергены'},
        ),
        migrations.AlterModelOptions(
            name='recipeingredient',
            options={'verbose_name': 'рецепт', 'verbose_name_plural': 'рецепты'},
        ),
        migrations.AlterField(
            model_name='allergen',
            name='name',
            field=models.CharField(max_length=25, verbose_name='Название алергена'),
        ),
    ]
