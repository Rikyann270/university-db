# Generated by Django 4.2 on 2024-04-21 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarships', '0003_courses_guide_job_tag_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Courses',
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='course_Abbreviation',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='sponsor',
            field=models.CharField(default='', max_length=50),
        ),
    ]
