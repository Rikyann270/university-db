# Generated by Django 4.2 on 2024-06-12 18:34

import assets.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Featured_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('featured_image', models.ImageField(blank=True, max_length=200, null=True, upload_to=assets.models.upload_location2)),
            ],
        ),
        migrations.CreateModel(
            name='Main_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_image', models.ImageField(blank=True, max_length=200, null=True, upload_to=assets.models.upload_location1)),
            ],
        ),
    ]
