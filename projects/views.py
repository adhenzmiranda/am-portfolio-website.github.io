from django.http import JsonResponse
from django.shortcuts import render
from .models import Projects 
from .serializer import ProjectsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def projects_page(request):
    return render(request, 'projects.html')

def project_detail_page(request, id):
    return render(request, 'project_detail.html')

@api_view(['GET', 'POST'])
def projects_list(request, format=None):
    if request.method == 'GET':
        projects = Projects.objects.all()
        serializer = ProjectsSerializer(projects, many=True)
        return JsonResponse({'projects':serializer.data})
    
    if request.method == 'POST':
        serializer = ProjectsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE']) 
def projects_detail(request, id, format=None):
    try:
        project = Projects.objects.get(pk=id)
    except Projects.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProjectsSerializer(project)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProjectsSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)