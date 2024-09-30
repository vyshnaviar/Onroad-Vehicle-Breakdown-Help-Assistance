# Generated by Django 5.0.7 on 2024-09-05 07:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onroad', '0026_alter_bikeservicerequest_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bikeservicerequest',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='bikeservicerequest',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='bikeservicerequest',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onroad.profile'),
        ),
    ]
