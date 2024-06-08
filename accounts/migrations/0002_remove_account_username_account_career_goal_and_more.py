# Generated by Django 4.2 on 2024-06-05 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_subject_subject'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='username',
        ),
        migrations.AddField(
            model_name='account',
            name='career_goal',
            field=models.CharField(blank=True, choices=[('Phd', 'Phd'), ('Diploma', 'Diploma'), ('Masters', 'Masters'), ('Bachelor', 'Bachelor'), ('Research', 'Research')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='citizenship',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='colleges_of_interest',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='degree_of_pursuit',
            field=models.CharField(blank=True, choices=[('Phd', 'Phd'), ('Diploma', 'Diploma'), ('Masters', 'Masters'), ('Bachelor', 'Bachelor'), ('Research', 'Research')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='ethnic_background',
            field=models.CharField(blank=True, choices=[('male', 'male'), ('female', 'female'), ('other', 'other')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='field_of_study',
            field=models.ManyToManyField(related_name='courses', to='courses.subject'),
        ),
        migrations.AddField(
            model_name='account',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'male'), ('female', 'female'), ('other', 'other')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='graduation_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='high_school_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='overall_GPA',
            field=models.CharField(blank=True, choices=[('Phd', 'Phd'), ('Diploma', 'Diploma'), ('Masters', 'Masters'), ('Bachelor', 'Bachelor'), ('Research', 'Research')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='presently_attending_college',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='account',
            name='school_level',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='second_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='zip_code',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='is_admin',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='is_superuser',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='phone_number',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
    ]
