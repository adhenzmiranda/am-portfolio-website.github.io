from django.db import models
from cloudinary.models import CloudinaryField
from multiselectfield import MultiSelectField

TECH_STACK_CHOICES = [
    ('Languages', [
        ('python', 'Python'),
        ('javascript', 'JavaScript'),
        ('html', 'HTML'),
        ('csharp', 'C#'),
        ('kotlin', 'Kotlin'),
    ]),
    ('Frameworks & Libraries', [
        ('scss', 'Sass'),
        ('django', 'Django'),
        ('gsap', 'GSAP'),
        ('cloudinary', 'Cloudinary'),
        ('nodejs', 'Node.js'),
        ('imgur', 'Imgur'),
    ]),
    ('Development Tools', [
        ('github', 'GitHub'),
        ('heroku', 'Heroku'),
        ('androidstudio', 'Android Studio'),
        ('cursor', 'Cursor'),
    ]),
    ('AI & Security Tools', [
        ('chatgpt', 'ChatGPT'),
        ('claude', 'Claude'),
        ('autopsy', 'Autopsy'),
        ('cisco', 'Cisco'),
        ('tryhackme', 'TryHackMe'),
    ]),
    ('Design & Creative', [
        ('figma', 'Figma'),
        ('photoshop', 'Photoshop'),
        ('illustrator', 'Illustrator'),
        ('lightroom', 'Lightroom'),
        ('canva', 'Canva'),
    ]),
    ('Video & Audio', [
        ('premiere', 'Premiere Pro'),
        ('aftereffects', 'After Effects'),
        ('audition', 'Audition'),
        ('davinci', 'DaVinci Resolve'),
    ]),
    ('Game Development', [
        ('unity', 'Unity'),
        ('twine', 'Twine'),
        ('harlowe', 'Harlowe'),
    ]),
]

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
    # Removed main_image for clarity. Only using one image field now.
    thumbnail_image = CloudinaryField('image', folder='thumbnails', blank=True, null=True,
        transformation=[
            {'width': 600, 'height': 338, 'crop': 'fill'},
            {'quality': 'auto', 'fetch_format': 'auto'}
        ])
    technologies = MultiSelectField(choices=TECH_STACK_CHOICES, blank=True, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + ' - ' + str(self.description)[:20] + '...'

    def get_technology_display(self, tech_value):
        # Flatten grouped choices for lookup
        flat_choices = []
        for group in TECH_STACK_CHOICES:
            flat_choices.extend(group[1])
        return dict(flat_choices).get(tech_value, tech_value)

class ProjectPhoto(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='photos')
    image = CloudinaryField('image', folder='project_photos',
        transformation=[
            {'width': 1920, 'height': 1080, 'crop': 'limit'},
            {'quality': 'auto', 'fetch_format': 'auto'}
        ])
    caption = models.CharField(max_length=200, blank=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'created_at']

    def __str__(self):
        return f"{self.project.name} - Photo {self.order}"

class ProjectEmbed(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='embeds')
    embed_code = models.TextField(
        help_text="Paste the full embed code (e.g., <iframe ...></iframe>) for a video or interactive media. Example: <iframe width='560' height='315' src='https://www.youtube.com/embed/VIDEO_ID' frameborder='0' allowfullscreen></iframe>"
    )
    caption = models.CharField(max_length=200, blank=True)  # <-- Add this line
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'created_at']

    def __str__(self):
        return f"Embed for {self.project.name} ({self.id})"