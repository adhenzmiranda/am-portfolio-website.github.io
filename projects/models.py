from django.db import models

class Projects(models.Model):
    name =  models.CharField(max_length=100, unique=True)
    description = models.TextField()
    year = models.IntegerField(default=2024)  # Add default value here
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
        default='Other'  # Add this default value
    )
    tags = models.CharField(max_length=100, blank=True)
    # image = models.ImageField(upload_to='../frontend/assets/images/projects', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)

    def __str__(self):
        return self.name + ' - ' + str(self.description)[:20] + '...'