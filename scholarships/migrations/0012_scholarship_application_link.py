# Generated by Django 4.2 on 2024-06-19 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarships', '0011_scholarship_application_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='scholarship',
            name='application_link',
            field=models.URLField(blank=True),
        ),
    ]
