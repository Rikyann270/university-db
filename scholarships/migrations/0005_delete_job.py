# Generated by Django 4.2 on 2024-04-27 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scholarships', '0004_rename_university_universitie'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Job',
        ),
    ]