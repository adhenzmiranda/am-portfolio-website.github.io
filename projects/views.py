from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Projects 
from .serializer import ProjectsSerializer
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def projects_page(request):
    projects = Projects.objects.all()
    # Group projects by year
    projects_by_year = {}
    for project in projects:
        if project.year not in projects_by_year:
            projects_by_year[project.year] = []
        projects_by_year[project.year].append(project)
    
    # Sort years in descending order
    sorted_years = sorted(projects_by_year.keys(), reverse=True)
    
    context = {
        'projects_by_year': projects_by_year,
        'sorted_years': sorted_years
    }
    return render(request, 'projects.html', context)

def project_detail_page(request, id):
    project = get_object_or_404(Projects, id=id)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)

@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, FormParser])
def projects_list(request, format=None):
    if request.method == 'GET':
        projects = Projects.objects.all()
        serializer = ProjectsSerializer(projects, many=True, context={'request': request})
        return JsonResponse({'projects': serializer.data})
    
    if request.method == 'POST':
        serializer = ProjectsSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@parser_classes([MultiPartParser, FormParser])
def projects_detail(request, id, format=None):
    try:
        project = Projects.objects.get(pk=id)
    except Projects.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProjectsSerializer(project, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProjectsSerializer(project, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)