# Generated by Django 5.0.1 on 2024-01-06 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_category_menu_item_order_ordered_item_delete_booking_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name_lang',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AddField(
            model_name='menu_item',
            name='describtion_lang',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='menu_item',
            name='name_lang',
            field=models.CharField(default=None, max_length=35),
        ),
    ]