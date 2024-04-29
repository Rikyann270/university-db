# Generated by Django 4.2 on 2024-04-29 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarships', '0006_scholarship_university_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='submitted_scholarship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('user', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=100)),
                ('nationality', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='eligibity',
            field=models.CharField(max_length=3000),
        ),
    ]
