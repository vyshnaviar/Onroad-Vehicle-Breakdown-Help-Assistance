# Generated by Django 5.0.7 on 2024-09-05 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onroad', '0029_bikeservicerequest_profile_carservicerequest_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bikeservicerequest',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='carservicerequest',
            name='profile',
        ),
    ]
