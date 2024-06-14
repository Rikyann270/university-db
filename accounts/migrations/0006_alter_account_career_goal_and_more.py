# Generated by Django 4.2 on 2024-06-06 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_account_field_of_study_account_field_of_study'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='career_goal',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='degree_of_pursuit',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='ethnic_background',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='gender',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='overall_GPA',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]