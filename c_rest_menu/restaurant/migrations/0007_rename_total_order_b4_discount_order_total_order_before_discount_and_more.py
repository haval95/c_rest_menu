# Generated by Django 5.0.1 on 2024-01-07 00:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0006_menu_item_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='total_order_b4_discount',
            new_name='total_order_before_discount',
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='menu_item',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_items', to='restaurant.category'),
        ),
    ]
