from rest_framework import serializers
from .models import Projects, ProjectPhoto

class ProjectPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectPhoto
        fields = ['id', 'image', 'caption', 'order']

class ProjectsSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    thumbnail_url = serializers.SerializerMethodField()
    photos = ProjectPhotoSerializer(many=True, read_only=True)
    
    class Meta:
        model = Projects
        fields = ['id', 'name', 'year', 'category', 'tags', 'description', 
                 'created_at', 'updated_at', 'image', 'thumbnail',
                 'image_url', 'thumbnail_url', 'photos']
    
    def get_image_url(self, obj):
        if obj.image:
            return self.context['request'].build_absolute_uri(obj.image.url)
        return None
        
    def get_thumbnail_url(self, obj):
        if obj.thumbnail:
            return self.context['request'].build_absolute_uri(obj.thumbnail.url)
        return None