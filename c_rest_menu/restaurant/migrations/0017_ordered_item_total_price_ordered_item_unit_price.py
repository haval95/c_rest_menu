# Generated by Django 5.0.1 on 2024-01-09 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0016_cart_cartitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordered_item',
            name='total_price',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='ordered_item',
            name='unit_price',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
