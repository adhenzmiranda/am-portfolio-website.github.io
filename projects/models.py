from django.db import models
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from io import BytesIO
from cloudinary.models import CloudinaryField

class YourModel(models.Model):
    image = CloudinaryField('image')

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
    image = CloudinaryField('image', folder='projects', blank=True, null=True)
    thumbnail = CloudinaryField('image', folder='thumbnails', blank=True, null=True)
    video_embed = models.TextField(
        blank=True,
        null=True,
        help_text="Paste the embed code from YouTube, Vimeo, or other video platforms. The code should start with <iframe>"
    )
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
                image.thumbnail(output_size, Image.Resampling.LANCZOS)
            
            # Create grid-optimized thumbnail
            # Base size for grid items (matching your SCSS minmax(300px, 1fr))
            thumbnail_width = 600  # 2x the minimum grid size for better quality
            thumbnail_height = int(thumbnail_width * 9 / 16)  # Maintain 16:9 ratio
            thumbnail_size = (thumbnail_width, thumbnail_height)
            
            thumb = image.copy()
            
            # Calculate the aspect ratio for 16:9
            target_ratio = 16 / 9
            current_ratio = thumb.width / thumb.height
            
            if current_ratio > target_ratio:
                # Image is wider than 16:9, crop the sides
                new_width = int(thumb.height * target_ratio)
                left = (thumb.width - new_width) // 2
                right = left + new_width
                thumb = thumb.crop((left, 0, right, thumb.height))
            else:
                # Image is taller than 16:9, crop the top and bottom
                new_height = int(thumb.width / target_ratio)
                top = (thumb.height - new_height) // 2
                bottom = top + new_height
                thumb = thumb.crop((0, top, thumb.width, bottom))
            
            # Resize to exact thumbnail size with high-quality settings
            thumb = thumb.resize(thumbnail_size, Image.Resampling.LANCZOS)
            
            # Save both images with high quality
            output = BytesIO()
            image.save(output, format='JPEG', quality=95, optimize=True)
            self.image = InMemoryUploadedFile(
                output,
                'ImageField',
                f"{self.name}_image.jpg",
                'image/jpeg',
                sys.getsizeof(output),
                None
            )
            
            thumb_output = BytesIO()
            thumb.save(thumb_output, format='JPEG', quality=95, optimize=True)
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

class ProjectPhoto(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='photos')
    image = CloudinaryField('image', folder='project_photos')
    caption = models.CharField(max_length=200, blank=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'created_at']

    def save(self, *args, **kwargs):
        if self.image:
            image = Image.open(self.image)
            
            # Convert image to RGB if it's not
            if image.mode != 'RGB':
                image = image.convert('RGB')
            
            # Resize image if it's too large
            if image.height > 1080 or image.width > 1920:
                output_size = (1920, 1080)
                image.thumbnail(output_size)
            
            output = BytesIO()
            image.save(output, format='JPEG', quality=90)
            self.image = InMemoryUploadedFile(
                output,
                'ImageField',
                f"{self.project.name}_photo_{self.order}.jpg",
                'image/jpeg',
                sys.getsizeof(output),
                None
            )
            
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.project.name} - Photo {self.order}"