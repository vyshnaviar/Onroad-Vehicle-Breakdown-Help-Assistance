# Generated by Django 5.0.7 on 2024-09-04 17:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onroad', '0023_bikeservicerequest_booking_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bikeservicerequest',
            name='customer_name',
        ),
        migrations.RemoveField(
            model_name='bikeservicerequest',
            name='phone_no',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='object_id',
        ),
        migrations.AddField(
            model_name='checkout',
            name='bike_service_request',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='onroad.bikeservicerequest'),
        ),
        migrations.AddField(
            model_name='checkout',
            name='car_service_request',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='onroad.carservicerequest'),
        ),
    ]
