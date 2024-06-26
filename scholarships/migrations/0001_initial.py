# Generated by Django 4.2 on 2024-05-14 16:51

from django.db import migrations, models
import scholarships.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='submitted_scholarship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('nationality', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Universitie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('University_Scholarship_image', models.ImageField(null=True, upload_to=scholarships.models.upload_location)),
            ],
        ),
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('University_name', models.CharField(default='', max_length=100)),
                ('Scholarship_image', models.ImageField(blank=True, null=True, upload_to=scholarships.models.upload_location2)),
                ('course', models.CharField(blank=True, max_length=100)),
                ('eligibity', models.CharField(max_length=3000)),
                ('country', models.CharField(max_length=100)),
                ('completion_time', models.DateField(blank=True, default='0001-01-1')),
                ('closing_date', models.DateField()),
                ('funding_status', models.CharField(choices=[('Fully funded', 'Fully funded'), ('Partially funded', 'Partially funded'), ('Underfunded', 'Underfunded'), ('Unfunded', 'Unfunded'), ('Self-funded', 'Self-funded')], max_length=100)),
                ('course_Abbreviation', models.CharField(blank=True, default='', max_length=100)),
                ('subject', models.CharField(blank=True, max_length=100)),
                ('sponsor', models.CharField(blank=True, default='', max_length=100)),
                ('applicants', models.IntegerField(default=0)),
                ('slug', models.SlugField(blank=True, max_length=200, unique=True)),
                ('degree', models.ManyToManyField(related_name='scholarships', to='scholarships.degree')),
                ('tags', models.ManyToManyField(related_name='scholarships', to='scholarships.tag')),
            ],
        ),
    ]
