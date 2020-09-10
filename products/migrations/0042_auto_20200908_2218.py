# Generated by Django 3.0.7 on 2020-09-08 22:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0041_product_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='user_rating',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=2, null=True),
        ),
    ]