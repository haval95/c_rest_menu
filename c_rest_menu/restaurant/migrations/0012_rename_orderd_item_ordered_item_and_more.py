# Generated by Django 5.0.1 on 2024-01-08 22:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0011_remove_order_items_alter_orderd_item_order'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='orderd_item',
            new_name='Ordered_item',
        ),
        migrations.RemoveField(
            model_name='order',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
        migrations.RemoveField(
            model_name='order',
            name='total_order_after_discount',
        ),
        migrations.RemoveField(
            model_name='order',
            name='total_order_before_discount',
        ),
    ]
