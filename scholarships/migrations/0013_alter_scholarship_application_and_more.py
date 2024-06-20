# Generated by Django 4.2 on 2024-06-20 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarships', '0012_scholarship_application_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scholarship',
            name='application',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='available_subjects',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='benefits',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='degree_level',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='description',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='eligible_criteria',
            field=models.CharField(blank=True, max_length=2000),
        ),
    ]
