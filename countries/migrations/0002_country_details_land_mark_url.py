# Generated by Django 4.2 on 2024-06-12 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='country_details',
            name='land_mark_url',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
    ]
