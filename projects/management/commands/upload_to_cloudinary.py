from django.core.management.base import BaseCommand
from django.conf import settings
import os
from cloudinary.uploader import upload
from projects.models import Projects, ProjectPhoto
from PIL import Image
from io import BytesIO

class Command(BaseCommand):
    help = 'Uploads existing media files to Cloudinary'

    def handle(self, *args, **options):
        media_root = settings.MEDIA_ROOT
        self.stdout.write(f"Media root: {media_root}")
        
        # Process project images
        projects_dir = os.path.join(media_root, 'projects')
        self.stdout.write(f"Looking for images in: {projects_dir}")
        
        if os.path.exists(projects_dir):
            for filename in os.listdir(projects_dir):
                if filename.endswith(('.png', '.jpg', '.jpeg')):
                    file_path = os.path.join(projects_dir, filename)
                    self.stdout.write(f"Processing file: {file_path}")
                    
                    try:
                        # Open and process image
                        with open(file_path, 'rb') as image_file:
                            # Upload to Cloudinary
                            upload_result = upload(
                                image_file,
                                folder="projects",
                                resource_type="image",
                                use_filename=True,
                                unique_filename=True
                            )
                            
                            self.stdout.write(f"Upload result: {upload_result}")
                            
                            # Create or update project
                            project_name = os.path.splitext(filename)[0]
                            project, created = Projects.objects.get_or_create(
                                name=project_name,
                                defaults={
                                    'description': f'Project {project_name}',
                                    'year': 2024
                                }
                            )
                            
                            # Update image field with public_id
                            project.image = upload_result['public_id']
                            project.save()
                            
                            self.stdout.write(
                                self.style.SUCCESS(f'Successfully uploaded {filename} to Cloudinary')
                            )
                    except Exception as e:
                        self.stdout.write(
                            self.style.ERROR(f'Error processing {filename}: {str(e)}')
                        )
                        import traceback
                        self.stdout.write(self.style.ERROR(traceback.format_exc()))

        # Process project photos
        photos_dir = os.path.join(media_root, 'project_photos')
        self.stdout.write(f"Looking for photos in: {photos_dir}")
        
        if os.path.exists(photos_dir):
            for filename in os.listdir(photos_dir):
                if filename.endswith(('.png', '.jpg', '.jpeg')):
                    file_path = os.path.join(photos_dir, filename)
                    self.stdout.write(f"Processing photo: {file_path}")
                    
                    try:
                        # Upload directly to Cloudinary
                        with open(file_path, 'rb') as image_file:
                            upload_result = upload(
                                image_file,
                                folder="project_photos",
                                resource_type="image",
                                use_filename=True,
                                unique_filename=True
                            )
                            
                            self.stdout.write(f"Upload result: {upload_result}")
                            
                            # Create project photo entry
                            photo = ProjectPhoto.objects.create(
                                project=Projects.objects.first(),  # You'll need to adjust this
                                image=upload_result['public_id'],
                                caption=f"Photo for {filename}"
                            )
                            
                            self.stdout.write(
                                self.style.SUCCESS(f'Successfully uploaded photo {filename} to Cloudinary')
                            )
                    except Exception as e:
                        self.stdout.write(
                            self.style.ERROR(f'Error processing photo {filename}: {str(e)}')
                        )
                        import traceback
                        self.stdout.write(self.style.ERROR(traceback.format_exc())) 