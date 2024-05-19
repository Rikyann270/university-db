# Generated by Django 4.2 on 2024-05-15 11:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarships', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(validators=[django.core.validators.URLValidator])),
                ('description', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='universitie',
            name='links',
            field=models.ManyToManyField(to='scholarships.link'),
        ),
    ]
