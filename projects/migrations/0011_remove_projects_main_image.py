# Generated by Django 5.2 on 2025-04-23 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_rename_image_projects_main_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='main_image',
        ),
    ]
