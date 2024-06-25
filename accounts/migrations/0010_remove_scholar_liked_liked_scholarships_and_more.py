# Generated by Django 4.2 on 2024-06-25 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarships', '0019_scholarship_likes'),
        ('accounts', '0009_scholar_liked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scholar_liked',
            name='liked_scholarships',
        ),
        migrations.AddField(
            model_name='scholar_liked',
            name='liked_scholarships',
            field=models.ManyToManyField(related_name='scholarships', to='scholarships.scholarship'),
        ),
    ]