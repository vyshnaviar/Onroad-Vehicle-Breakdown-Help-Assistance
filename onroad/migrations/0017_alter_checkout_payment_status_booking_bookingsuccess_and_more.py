# Generated by Django 5.0.7 on 2024-07-25 19:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onroad', '0016_remove_bookingsuccess_booking_servicerequest_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='payment_status',
            field=models.CharField(default='Success', max_length=20),
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_type', models.CharField(choices=[('towing', 'Towing'), ('tire_replacement', 'Tire Replacement'), ('fuel_delivery', 'Fuel Delivery'), ('battery_jumpstart', 'Battery Jumpstart'), ('flat_tyre', 'Flat Tyre'), ('general_services', 'General Services'), ('starting_problem', 'Starting Problem'), ('fitment_service', 'Fitment Service'), ('key_unlock_assistance', 'Key-Unlock Assistance')], max_length=30)),
                ('booking_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='Pending', max_length=20)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onroad.profile')),
            ],
        ),
        migrations.CreateModel(
            name='BookingSuccess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirmation_message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('booking', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='onroad.booking')),
            ],
        ),
        migrations.DeleteModel(
            name='ServiceRequest',
        ),
    ]
