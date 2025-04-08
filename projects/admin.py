from django.contrib import admin
from django.utils.html import format_html
from .models import Projects

@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'year', 'display_thumbnail', 'created_at')
    list_filter = ('category', 'year')
    search_fields = ('name', 'description', 'tags')
    readonly_fields = ('display_thumbnail',)

    def display_thumbnail(self, obj):
        if obj.thumbnail:
            return format_html('<img src="{}" width="50" height="50" />', obj.thumbnail.url)
        return "No thumbnail"
    display_thumbnail.short_description = 'Thumbnail'