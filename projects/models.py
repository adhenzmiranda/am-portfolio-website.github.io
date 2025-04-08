from django.db import models
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from io import BytesIO

class Projects(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    year = models.IntegerField(default=2024)
    category = models.CharField(
        max_length=50, 
        choices=[
            ('Web Development', 'Web Development'),
            ('Mobile Development', 'Mobile Development'),
            ('Data Science', 'Data Science'),
            ('Machine Learning', 'Machine Learning'),
            ('Game Development', 'Game Development'),
            ('Graphic Design', 'Graphic Design'),
            ('Website Design', 'Website Design'),
            ('Other', 'Other')
        ],
        default='Other'
    )
    tags = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Process the main image
        if self.image:
            image = Image.open(self.image)
            
            # Convert image to RGB if it's not
            if image.mode != 'RGB':
                image = image.convert('RGB')
            
            # Resize main image if it's too large
            if image.height > 1080 or image.width > 1920:
                output_size = (1920, 1080)
                image.thumbnail(output_size)
            
            # Create thumbnail
            thumbnail_size = (300, 300)
            thumb = image.copy()
            thumb.thumbnail(thumbnail_size)
            
            # Save both images
            output = BytesIO()
            image.save(output, format='JPEG', quality=90)
            self.image = InMemoryUploadedFile(
                output,
                'ImageField',
                f"{self.name}_image.jpg",
                'image/jpeg',
                sys.getsizeof(output),
                None
            )
            
            thumb_output = BytesIO()
            thumb.save(thumb_output, format='JPEG', quality=90)
            self.thumbnail = InMemoryUploadedFile(
                thumb_output,
                'ImageField',
                f"{self.name}_thumb.jpg",
                'image/jpeg',
                sys.getsizeof(thumb_output),
                None
            )
            
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name + ' - ' + str(self.description)[:20] + '...'