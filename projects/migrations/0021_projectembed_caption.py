# Generated by Django 5.2 on 2025-04-30 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0020_alter_projects_technologies'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectembed',
            name='caption',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
