# Generated by Django 5.0.7 on 2024-07-19 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onroad', '0004_alter_bikeservicerequest_services_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
