# Generated by Django 5.0.7 on 2024-09-04 12:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('onroad', '0020_rename_username_bikeservicerequest_customer_name_and_more'),
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
            model_name='carservicerequest',
            name='customer_name',
        ),
        migrations.RemoveField(
            model_name='carservicerequest',
            name='phone_no',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='booking_status',
        ),
        migrations.AddField(
            model_name='bikeservicerequest',
            name='booking_status',
            field=models.CharField(default='Pending', max_length=20),
        ),
        migrations.AddField(
            model_name='bikeservicerequest',
            name='profile',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='bike_service_requests', to='onroad.profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bikeservicerequest',
            name='requested_at',
            field=models.DateTimeField(auto_now_add=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carservicerequest',
            name='booking_status',
            field=models.CharField(default='Pending', max_length=20),
        ),
        migrations.AddField(
            model_name='carservicerequest',
            name='profile',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='car_service_requests', to='onroad.profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carservicerequest',
            name='requested_at',
            field=models.DateTimeField(auto_now_add=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='checkout',
            name='content_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='checkout',
            name='object_id',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
