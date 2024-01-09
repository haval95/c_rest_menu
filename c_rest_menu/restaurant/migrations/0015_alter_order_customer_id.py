# Generated by Django 5.0.1 on 2024-01-09 01:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0014_rename_time_order_created_at_order_discount_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
