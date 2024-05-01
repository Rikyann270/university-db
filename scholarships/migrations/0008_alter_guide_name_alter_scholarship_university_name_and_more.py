# Generated by Django 4.2 on 2024-04-29 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarships', '0007_submitted_scholarship_alter_scholarship_eligibity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guide',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='University_name',
            field=models.CharField(default='DEFAULT', max_length=100),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='country',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='course',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='degree',
            field=models.CharField(choices=[('Phd', 'Phd'), ('Diploma', 'Diploma'), ('Masters', 'Masters'), ('Bachelor', 'Bachelor')], max_length=100),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='funding_status',
            field=models.CharField(choices=[('Fully funded', 'Fully funded'), ('Partially funded', 'Partially funded'), ('Underfunded', 'Underfunded'), ('Unfunded', 'Unfunded'), ('Self-funded', 'Self-funded')], max_length=100),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='sponsor',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='submitted_scholarship',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='submitted_scholarship',
            name='nationality',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='submitted_scholarship',
            name='user',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='universitie',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
