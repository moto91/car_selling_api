# Generated by Django 5.0.2 on 2024-03-08 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carad',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
    ]
