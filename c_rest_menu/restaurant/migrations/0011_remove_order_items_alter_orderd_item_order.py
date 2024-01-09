# Generated by Django 5.0.1 on 2024-01-08 22:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0010_orderd_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='items',
        ),
        migrations.AlterField(
            model_name='orderd_item',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.order'),
        ),
    ]
