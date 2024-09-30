# Generated by Django 5.0.7 on 2024-09-05 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onroad', '0027_alter_bikeservicerequest_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carservicerequest',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='carservicerequest',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='bikeservicerequest',
            name='booking_status',
        ),
        migrations.RemoveField(
            model_name='bikeservicerequest',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='bikeservicerequest',
            name='requested_at',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='bike_service_request',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='car_service_request',
        ),
        migrations.AddField(
            model_name='bikeservicerequest',
            name='customer_name',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bikeservicerequest',
            name='phone_no',
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carservicerequest',
            name='customer_name',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carservicerequest',
            name='phone_no',
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='checkout',
            name='booking_status',
            field=models.CharField(default='Success', max_length=20),
        ),
        migrations.RemoveField(
            model_name='carservicerequest',
            name='booking_status',
        ),
        migrations.RemoveField(
            model_name='carservicerequest',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='carservicerequest',
            name='requested_at',
        ),
    ]
