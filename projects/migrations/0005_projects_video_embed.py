# Generated by Django 4.2.10 on 2025-04-21 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_projectphoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='video_embed',
            field=models.TextField(blank=True, help_text='Paste the embed code from YouTube, Vimeo, or other video platforms. The code should start with <iframe>', null=True),
        ),
    ]
