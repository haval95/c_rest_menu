# Generated by Django 5.0 on 2023-12-28 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
