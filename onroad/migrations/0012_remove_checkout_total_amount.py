# Generated by Django 5.0.7 on 2024-07-25 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onroad', '0011_bookingsuccess_checkout'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='total_amount',
        ),
    ]
