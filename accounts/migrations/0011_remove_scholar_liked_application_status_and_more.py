# Generated by Django 4.2 on 2024-06-25 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_remove_scholar_liked_liked_scholarships_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scholar_liked',
            name='application_status',
        ),
        migrations.RemoveField(
            model_name='scholar_liked',
            name='liked_scholarships',
        ),
        migrations.AddField(
            model_name='scholar_liked',
            name='liked_scholarship',
            field=models.CharField(default='', max_length=160),
        ),
        migrations.AddField(
            model_name='scholar_liked',
            name='liked_scholarship_slug',
            field=models.CharField(default='', max_length=230),
        ),
    ]