# Generated by Django 4.2 on 2024-04-29 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('premium', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Consultations',
            new_name='Consultation',
        ),
        migrations.RenameField(
            model_name='consultation',
            old_name='course_consultations',
            new_name='course_Consultation',
        ),
    ]