"""
URL configuration for projects project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from projects import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.shortcuts import render

# Define a view to serve the index.html file
def homepage(request):
    return render(request, 'index.html')  # Render the index.html file

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),  # Serve index.html at the root path
    path('projects/', views.projects_list),
    path('projects/<int:id>', views.projects_detail),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)
